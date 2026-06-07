# funcoes relacionadas ao cadastro e gerenciamentos dos usuários!

import dados
from constantes import ID_INICIAL_USUARIO
from auxiliares import cabecalho, linha
from emprestimos import contar_emprestimos_usuario


def gerar_id_usuario():
    #gera um ID unico para cada usuarios
    return ID_INICIAL_USUARIO + len(dados.usuarios)


def buscar_usuario_por_id(usuario_id):
    
    for usuario in dados.usuarios:
        if usuario["id"] == usuario_id:
            return usuario #se estiver no if ele retorna o dicionários dos usuários, 
    return None #se não estiver no if, ele retorna none


def cadastrar_usuario():
    #cadastra um novo user
    cabecalho("CADASTRAR USUÁRIO")
    nome  = input("  Nome completo: ").strip()
    email = input("  E-mail: ").strip()
    fone  = input("  Telefone: ").strip()
    cpf   = input("  CPF (opcional): ").strip()
    turma = input("  Turma/Curso: ").strip()

    if not nome:
        print("\nNome é obrigatório!")
        return

    usuario = {
        "id":               gerar_id_usuario(),
        "nome":             nome,
        "email":            email,
        "telefone":         fone,
        "cpf":              cpf,
        "turma":            turma,
        "multa_acumulada":  0.0,
    }
    dados.usuarios.append(usuario)
    print(f"\nUsuário '{nome}' cadastrado com ID {usuario['id']}.")


def listar_usuarios():
    #lista todos os usuarios
    cabecalho("USUÁRIOS CADASTRADOS")
    if not dados.usuarios:
        print("  Nenhum usuário cadastrado ainda.")
        return
    for user in dados.usuarios: 
        ativos = contar_emprestimos_usuario(user["id"])
        print(f"  [{user['id']}] {user['nome']} | {user['email']}") 
        print(f"       Empréstimos ativos: {ativos} | Multa: R$ {user['multa_acumulada']:.2f}")
        linha("-", 55)


def pagar_multa():
    #registra o pagamento da multa de um usuário
    cabecalho("PAGAR MULTA")
    userid = input("  ID do usuário: ").strip()
    if not userid.isdigit(): #is digit é para verificar se a string digitada contém numbers
        print("  ID inválido.")
        return
    usuario = buscar_usuario_por_id(int(userid))
    if not usuario:
        print("  Usuário não encontrado.")
        return
    if usuario["multa_acumulada"] <= 0:
        print(f"  {usuario['nome']} não possui multa pendente.")
        return
    print(f"  Multa de R$ {usuario['multa_acumulada']:.2f} para {usuario['nome']}.")
    confirmar = input("  Confirmar pagamento? (s/n): ").strip().lower()
    if confirmar == "s":
        usuario["multa_acumulada"] = 0.0
        print("Multa paga com sucesso!")
