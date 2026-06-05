# livros.py
# Funções relacionadas ao cadastro e consulta de livros

import dados
from constantes import ID_INICIAL_LIVRO
from auxiliares import cabecalho, linha


def gerar_id_livro(): #Vai gerar um ID unico pro novo livro 
    return ID_INICIAL_LIVRO + len(dados.livros)

def buscar_livro_por_id(livro_id): #Retorna o dicionário do livro com esse ID ou None
    for livro in dados.livros:
        if livro["id"] == livro_id:
            return livro
    return None

def cadastrar_livro(): #Cadastra um novo livro na biblioteca
    cabecalho("CADASTRAR LIVRO")
    titulo  = input("Título do livro: ").strip()
    autor   = input("Autor: ").strip()
    ano     = input("Ano de publicação: ").strip()
    genero  = input("Gênero/Categoria: ").strip()
    editora = input("Editora: ").strip()
    qtd     = input("Quantidade de exemplares: ").strip()

    if not titulo or not autor:
        print("\nTítulo e autor são obrigatórios.")
        return
    qtd = int(qtd) if qtd.isdigit() else 1

    livro = {
        "id":                    gerar_id_livro(),
        "titulo":                titulo,
        "autor":                 autor,
        "ano":                   ano,
        "genero":                genero,
        "editora":               editora,
        "quantidade_total":      qtd,
        "quantidade_disponivel": qtd,
    }
    dados.livros.append(livro)
    print(f"\nLivro '{titulo}' cadastrado com ID {livro['id']}.")


def listar_livros():  #Lista todos os livros do acervo
    cabecalho("ACERVO DE LIVROS")
    if not dados.livros:
        print("  Nenhum livro cadastrado ainda.")
        return
    for livro in dados.livros:
        status = "Disponível" if livro["quantidade_disponivel"] > 0  else "Indisponível"
        print(f"[{livro['id']}] {livro['titulo']} - {livro['autor']} ({livro['ano']})")
        print(f"Gênero: {livro['genero']} | Exemplares: {livro['quantidade_disponivel']}/{livro['quantidade_total']} | {status}")
        linha("-", 55)


def pesquisar_livro(): #Pesquisa livro por título, autor ou gênero
    cabecalho("PESQUISAR LIVRO")
    print("Filtrar por: (1) Título  (2) Autor  (3) Gênero")
    filtro = input("Escolha o filtro: ").strip()
    termo  = input(" Digite o termo de busca: ").strip().lower()

    if filtro == "1":
        encontrados = [l for l in dados.livros if termo in l["titulo"].lower()]
    elif filtro == "2":
        encontrados = [l for l in dados.livros if termo in l["autor"].lower()]
    elif filtro == "3":
        encontrados = [l for l in dados.livros if termo in l["genero"].lower()]
    else:
        encontrados = [l for l in dados.livros if termo in l["titulo"].lower() or termo in l["autor"].lower()]

    if not encontrados:
        print("Nenhum livro encontrado.")
        return
    for livro in encontrados:
        print(f"[{livro['id']}] {livro['titulo']} - {livro['autor']}")
