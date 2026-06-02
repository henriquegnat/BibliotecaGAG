import os
import datetime
import math
import random
import time

# ========== CONSTANTES ==========
LIMITE_EMPRESTIMOS = 3
DIAS_PRAZO = 7
MULTA_POR_DIA = 2.50
TAXA_CADASTRO = 0.0

# ========== LISTAS E DICIONÁRIOS ==========
livros = []
usuarios = []
emprestimos = []
historico = []


# ========== FUNÇÕES UTILITÁRIAS ==========

def pausar():
    input("\nPressione ENTER para continuar...")

def linha():
    print("-" * 40)


# ========== FUNÇÕES DE LIVRO ==========

def cadastrar_livro():
    print("\n--- CADASTRAR LIVRO ---")
    titulo = input("Titulo do livro: ")
    autor = input("Autor: ")
    ano = input("Ano de publicacao: ")
    genero = input("Genero: ")
    quantidade = int(input("Quantidade de exemplares: "))

    livro = {
        "id": len(livros) + 1,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "genero": genero,
        "total": quantidade,
        "disponivel": quantidade
    }

    livros.append(livro)
    print("Livro cadastrado com sucesso! ID:", livro["id"])


def listar_livros():
    print("\n--- ACERVO DE LIVROS ---")
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for i in range(len(livros)):
        livro = livros[i]
        print("ID:", livro["id"], "| Titulo:", livro["titulo"], "| Autor:", livro["autor"], "| Disponivel:", livro["disponivel"], "/", livro["total"])


def buscar_livro():
    print("\n--- BUSCAR LIVRO ---")
    termo = input("Digite parte do titulo ou autor: ")
    encontrou = False

    for i in range(len(livros)):
        livro = livros[i]
        if termo.lower() in livro["titulo"].lower() or termo.lower() in livro["autor"].lower():
            print("ID:", livro["id"], "| Titulo:", livro["titulo"], "| Autor:", livro["autor"], "| Ano:", livro["ano"])
            encontrou = True

    if not encontrou:
        print("Nenhum livro encontrado.")


# ========== FUNÇÕES DE USUÁRIO ==========

def cadastrar_usuario():
    print("\n--- CADASTRAR USUARIO ---")
    nome = input("Nome completo: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    tipo = input("Tipo (1-Aluno / 2-Professor): ")
    if tipo == "1":
        tipo_nome = "Aluno"
    else:
        tipo_nome = "Professor"

    usuario = {
        "id": len(usuarios) + 1,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "tipo": tipo_nome,
        "multa": 0.0
    }

    usuarios.append(usuario)
    print("Usuario cadastrado com sucesso! ID:", usuario["id"])


def listar_usuarios():
    print("\n--- USUARIOS CADASTRADOS ---")
    if len(usuarios) == 0:
        print("Nenhum usuario cadastrado.")
        return

    for i in range(len(usuarios)):
        u = usuarios[i]
        print("ID:", u["id"], "| Nome:", u["nome"], "| Tipo:", u["tipo"], "| Multa: R$", u["multa"])


def buscar_usuario_por_id(uid):
    for i in range(len(usuarios)):
        if usuarios[i]["id"] == uid:
            return usuarios[i]
    return None


def buscar_livro_por_id(lid):
    for i in range(len(livros)):
        if livros[i]["id"] == lid:
            return livros[i]
    return None


# ========== FUNÇÕES DE EMPRÉSTIMO ==========

def contar_emprestimos_usuario(uid):
    contador = 0
    for i in range(len(emprestimos)):
        if emprestimos[i]["usuario_id"] == uid:
            contador += 1
    return contador


def realizar_emprestimo():
    print("\n--- REALIZAR EMPRESTIMO ---")

    listar_usuarios()
    uid = int(input("\nDigite o ID do usuario: "))
    usuario = buscar_usuario_por_id(uid)

    if usuario is None:
        print("Usuario nao encontrado.")
        return

    if usuario["multa"] > 0:
        print("Usuario tem multa pendente de R$", usuario["multa"], ". Quite antes de emprestar.")
        return

    total = contar_emprestimos_usuario(uid)
    if total >= LIMITE_EMPRESTIMOS:
        print("Usuario ja atingiu o limite de", LIMITE_EMPRESTIMOS, "emprestimos.")
        return

    listar_livros()
    lid = int(input("\nDigite o ID do livro: "))
    livro = buscar_livro_por_id(lid)

    if livro is None:
        print("Livro nao encontrado.")
        return

    if livro["disponivel"] <= 0:
        print("Livro indisponivel no momento.")
        return

    hoje = datetime.date.today()
    prazo = hoje + datetime.timedelta(days=DIAS_PRAZO)

    emprestimo = {
        "livro_id": lid,
        "usuario_id": uid,
        "data_emprestimo": str(hoje),
        "data_prazo": str(prazo)
    }

    emprestimos.append(emprestimo)
    livro["disponivel"] -= 1

    print("\nEmprestimo realizado!")
    print("Livro:", livro["titulo"])
    print("Usuario:", usuario["nome"])
    print("Prazo de devolucao:", prazo.strftime("%d/%m/%Y"))


def devolver_livro():
    print("\n--- DEVOLVER LIVRO ---")

    listar_usuarios()
    uid = int(input("\nDigite o ID do usuario: "))
    usuario = buscar_usuario_por_id(uid)

    if usuario is None:
        print("Usuario nao encontrado.")
        return

    # listar emprestimos do usuario
    emp_usuario = []
    for i in range(len(emprestimos)):
        if emprestimos[i]["usuario_id"] == uid:
            emp_usuario.append(emprestimos[i])

    if len(emp_usuario) == 0:
        print("Esse usuario nao tem emprestimos ativos.")
        return

    print("\nLivros emprestados para", usuario["nome"], ":")
    for i in range(len(emp_usuario)):
        livro = buscar_livro_por_id(emp_usuario[i]["livro_id"])
        print("ID:", livro["id"], "| Titulo:", livro["titulo"], "| Prazo:", emp_usuario[i]["data_prazo"])

    lid = int(input("\nDigite o ID do livro a devolver: "))
    livro = buscar_livro_por_id(lid)

    emp_encontrado = None
    for i in range(len(emp_usuario)):
        if emp_usuario[i]["livro_id"] == lid:
            emp_encontrado = emp_usuario[i]
            break

    if emp_encontrado is None:
        print("Emprestimo nao encontrado.")
        return

    hoje = datetime.date.today()
    prazo = datetime.date.fromisoformat(emp_encontrado["data_prazo"])

    multa = 0.0
    dias_atraso = 0

    if hoje > prazo:
        dias_atraso = (hoje - prazo).days
        multa = round(dias_atraso * MULTA_POR_DIA, 2)
        usuario["multa"] = round(usuario["multa"] + multa, 2)
        print("Devolucao com", dias_atraso, "dia(s) de atraso.")
        print("Multa gerada: R$", multa)
    else:
        print("Devolucao no prazo. Sem multa!")

    registro = {
        "livro": livro["titulo"],
        "usuario": usuario["nome"],
        "data_devolucao": str(hoje),
        "multa": multa
    }
    historico.append(registro)

    emprestimos.remove(emp_encontrado)
    livro["disponivel"] += 1

    print("Livro", livro["titulo"], "devolvido com sucesso!")


def pagar_multa():
    print("\n--- PAGAR MULTA ---")

    listar_usuarios()
    uid = int(input("\nDigite o ID do usuario: "))
    usuario = buscar_usuario_por_id(uid)

    if usuario is None:
        print("Usuario nao encontrado.")
        return

    if usuario["multa"] <= 0:
        print("Usuario nao tem multa pendente.")
        return

    print("Multa de", usuario["nome"], ": R$", usuario["multa"])
    confirma = input("Confirmar pagamento? (s/n): ")

    if confirma == "s":
        usuario["multa"] = 0.0
        print("Multa paga com sucesso!")
    else:
        print("Pagamento cancelado.")


def ver_emprestimos_ativos():
    print("\n--- EMPRESTIMOS ATIVOS ---")

    if len(emprestimos) == 0:
        print("Nenhum emprestimo ativo.")
        return

    hoje = datetime.date.today()

    for i in range(len(emprestimos)):
        emp = emprestimos[i]
        livro = buscar_livro_por_id(emp["livro_id"])
        usuario = buscar_usuario_por_id(emp["usuario_id"])
        prazo = datetime.date.fromisoformat(emp["data_prazo"])

        if hoje > prazo:
            dias = (hoje - prazo).days
            status = "ATRASADO " + str(dias) + " dia(s)"
        else:
            status = "No prazo"

        print("Livro:", livro["titulo"], "| Usuario:", usuario["nome"], "| Prazo:", emp["data_prazo"], "| Status:", status)


# ========== RELATÓRIO ==========

def mostrar_relatorio():
    print("\n--- RELATORIO DA BIBLIOTECA ---")
    print("Data:", datetime.date.today().strftime("%d/%m/%Y"))
    linha()

    total_exemplares = 0
    total_disponiveis = 0
    for i in range(len(livros)):
        total_exemplares += livros[i]["total"]
        total_disponiveis += livros[i]["disponivel"]

    print("Livros cadastrados :", len(livros))
    print("Total de exemplares:", total_exemplares)
    print("Disponiveis        :", total_disponiveis)
    print("Emprestados        :", total_exemplares - total_disponiveis)

    total_multas = 0.0
    for i in range(len(usuarios)):
        total_multas += usuarios[i]["multa"]

    linha()
    print("Usuarios cadastrados:", len(usuarios))
    print("Emprestimos ativos  :", len(emprestimos))
    print("Devolucoes realizadas:", len(historico))
    print("Total de multas     : R$", round(total_multas, 2))


def salvar_relatorio():
    arquivo = open("relatorio_biblioteca.txt", "w")

    arquivo.write("RELATORIO FINAL - SISTEMA DE BIBLIOTECA\n")
    arquivo.write("Gerado em: " + str(datetime.date.today()) + "\n")
    arquivo.write("=" * 40 + "\n\n")

    arquivo.write("LIVROS:\n")
    for i in range(len(livros)):
        livro = livros[i]
        arquivo.write("  [" + str(livro["id"]) + "] " + livro["titulo"] + " - " + livro["autor"] + " (" + livro["ano"] + ")\n")
        arquivo.write("      Disponivel: " + str(livro["disponivel"]) + "/" + str(livro["total"]) + "\n")

    arquivo.write("\nUSUARIOS:\n")
    for i in range(len(usuarios)):
        u = usuarios[i]
        arquivo.write("  [" + str(u["id"]) + "] " + u["nome"] + " (" + u["tipo"] + ") | Multa: R$ " + str(u["multa"]) + "\n")

    arquivo.write("\nEMPRESTIMOS ATIVOS:\n")
    if len(emprestimos) == 0:
        arquivo.write("  Nenhum.\n")
    else:
        for i in range(len(emprestimos)):
            emp = emprestimos[i]
            livro = buscar_livro_por_id(emp["livro_id"])
            usuario = buscar_usuario_por_id(emp["usuario_id"])
            arquivo.write("  " + livro["titulo"] + " -> " + usuario["nome"] + " | Prazo: " + emp["data_prazo"] + "\n")

    arquivo.write("\nHISTORICO DE DEVOLUCOES:\n")
    if len(historico) == 0:
        arquivo.write("  Nenhuma devolucao.\an")
    else:
        for i in range(len(historico)):
            reg = historico[i]
            arquivo.write("  " + reg["livro"] + " devolvido por " + reg["usuario"] + " em " + reg["data_devolucao"])
            if reg["multa"] > 0:
                arquivo.write(" | Multa: R$ " + str(reg["multa"]))
            arquivo.write("\n")

    arquivo.write("\n" + "=" * 40 + "\n")
    arquivo.write("Fim do relatorio.\n")
    arquivo.close()

    print("Relatorio salvo em 'relatorio_biblioteca.txt'!")


# ========== INTRODUÇÃO ==========

def introducao():
    print("=" * 40)
    print("   SISTEMA DE BIBLIOTECA - PUC-PR")
    print("=" * 40)
    print()
    print("Bem-vindo, bibliotecario!")
    print()
    print("Neste sistema voce pode:")
    print("  - Cadastrar livros e usuarios")
    print("  - Realizar emprestimos e devolucoes")
    print("  - Controlar multas por atraso")
    print("  - Gerar relatorio ao encerrar")
    print()
    print("Regras:")
    print("  Limite de emprestimos por usuario:", LIMITE_EMPRESTIMOS)
    print("  Prazo de devolucao:", DIAS_PRAZO, "dias")
    print("  Multa por dia de atraso: R$", MULTA_POR_DIA)
    print()
    input("Pressione ENTER para comecar...")


# ========== MENU PRINCIPAL ==========

def menu():
    print("\n" + "=" * 40)
    print("         MENU PRINCIPAL")
    print("=" * 40)
    print("  [1]  Cadastrar livro")
    print("  [2]  Listar livros")
    print("  [3]  Buscar livro")
    print("  [4]  Cadastrar usuario")
    print("  [5]  Listar usuarios")
    print("  [6]  Realizar emprestimo")
    print("  [7]  Devolver livro")
    print("  [8]  Pagar multa")
    print("  [9]  Ver emprestimos ativos")
    print("  [10] Ver relatorio")
    print("  [0]  Sair")
    print("=" * 40)
    opcao = input("Digite sua opcao: ")
    return opcao


# ========== EXECUÇÃO PRINCIPAL ==========

introducao()

rodando = True
while rodando:
    opcao = menu()

    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        buscar_livro()
    elif opcao == "4":
        cadastrar_usuario()
    elif opcao == "5":
        listar_usuarios()
    elif opcao == "6":
        realizar_emprestimo()
    elif opcao == "7":
        devolver_livro()
    elif opcao == "8":
        pagar_multa()
    elif opcao == "9":
        ver_emprestimos_ativos()
    elif opcao == "10":
        mostrar_relatorio()
    elif opcao == "0":
        print("\nEncerrando o sistema...")
        mostrar_relatorio()
        salvar_relatorio()
        print("\nAte logo!")
        rodando = False
    else:
        print("Opcao invalida!")

    if rodando:
        pausar()