import os  # carrega biblioteca pra limpar tela

def linha (char="-", largura=55):  
    print(char * largura) 

def cabecalho(titulo):  # enfeita o titulo do menu
    linha("=")  
    print(f"{titulo}") 
    linha("=")  
def limpar_tela():  # apaga o terminal
    os.system("cls" if os.name == "nt" else "clear")  # comando pro windows ou linux/mac

def pausar():  # segura a tela
    input("\n Pressione ENTER para continuar...")  