# main.py
# Arquivo principal — apenas roda o sistema

from auxiliares import cabecalho, limpar_tela, pausar, linha
from livros import cadastrar_livro, listar_livros, pesquisar_livro
from usuarios import cadastrar_usuario, listar_usuarios, pagar_multa
from emprestimos import realizar_emprestimo, devolver_livro, listar_emprestimos
from relatorios import mostrar_relatorio, salvar_relatorio


# ── Introdução ───────────────────────────────────────────────────────────────

def introducao():
    """Mensagem de boas-vindas ao sistema."""
    limpar_tela()
    linha("═")
    print("  BEM-VINDO AO SISTEMA DE BIBLIOTECA - PUCPR")
    linha("═")
    print("""
  Você é o bibliotecário responsável por manter tudo
  em ordem. Com este sistema você pode:

    📚 Cadastrar e consultar livros do acervo
    👤 Gerenciar usuários e suas multas
    🔄 Controlar empréstimos e devoluções
    📄 Gerar relatórios da biblioteca

  Regras:
    • Limite de 3 livros por usuário
    • Prazo de devolução: 14 dias
    • Multa por atraso: R$ 2,50 por dia
    • Teto de multa: R$ 50,00
  """)
    input("  Pressione Enter para começar...")


# ── Encerramento ─────────────────────────────────────────────────────────────

def encerrar():
    """Salva o relatório e exibe mensagem de encerramento."""
    cabecalho("ENCERRANDO O SISTEMA")
    print("  Salvando relatório final...")
    arquivo = salvar_relatorio()
    print(f"\n  Obrigado por usar o Sistema de Biblioteca!")
    print(f"  Relatório salvo em: {arquivo}")
    linha("═")


# ── Submenus ─────────────────────────────────────────────────────────────────

def menu_livros():
    while True:                        # repetição 2
        limpar_tela()
        cabecalho("MENU - LIVROS")
        print("  (1) Cadastrar livro")
        print("  (2) Listar acervo")
        print("  (3) Pesquisar livro")
        print("  (0) Voltar")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            pesquisar_livro()
        elif opcao == "0":
            break
        else:
            print("  Opção inválida.")
        pausar()


def menu_usuarios():
    while True:                        # repetição 3
        limpar_tela()
        cabecalho("MENU - USUÁRIOS")
        print("  (1) Cadastrar usuário")
        print("  (2) Listar usuários")
        print("  (3) Pagar multa")
        print("  (0) Voltar")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            pagar_multa()
        elif opcao == "0":
            break
        else:
            print("  Opção inválida.")
        pausar()


def menu_emprestimos():
    while True:                        # repetição 4
        limpar_tela()
        cabecalho("MENU - EMPRÉSTIMOS")
        print("  (1) Realizar empréstimo")
        print("  (2) Devolver livro")
        print("  (3) Ver empréstimos ativos")
        print("  (0) Voltar")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            realizar_emprestimo()
        elif opcao == "2":
            devolver_livro()
        elif opcao == "3":
            listar_emprestimos()
        elif opcao == "0":
            break
        else:
            print("  Opção inválida.")
        pausar()


# ── Loop principal ────────────────────────────────────────────────────────────

def main():
    introducao()                       # INTRODUÇÃO

    while True:                        # repetição 1 — loop principal
        limpar_tela()
        cabecalho("MENU PRINCIPAL")
        print("  (1) Livros")
        print("  (2) Usuários")
        print("  (3) Empréstimos")
        print("  (4) Relatório")
        print("  (0) Sair")
        opcao = input("\n  Escolha uma opção: ").strip()

        if opcao == "1":
            menu_livros()
        elif opcao == "2":
            menu_usuarios()
        elif opcao == "3":
            menu_emprestimos()
        elif opcao == "4":
            mostrar_relatorio()
            pausar()
        elif opcao == "0":
            encerrar()                 # FIM
            break
        else:
            print("  Opção inválida. Tente novamente.")
            pausar()


if __name__ == "__main__":
    main()
