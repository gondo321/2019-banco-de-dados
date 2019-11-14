# importaçao da biblioteca
import sqlite3
import tabelaEstado
import tabelaCidade
import tabelaCliente
import tabelaTransporte



#Criaçao do Menu
def Menu():
    while(True):
print("""

    -----Menu-----\t\t
    
    1 - Cadastra do cliente
    2 - Logar
    3 - Alterar produto
    4 - Deletar produto
    5 - Sair
""")
    #Opeção Menu
    opcaoMenu = int(imput("Digite a opção que deseje: "))


    #Criaçao do cadastro do cliente
   
    if(opcaoMenu == 1):
        tabelaEstado.inserir_dados(conexao)
        tabelaCidade.Inserir_dados(conexao)
        tabelaCliente.Inserir_dados(conexao)
        tabelaTransporte.Inserir_dados(conexao)

    #Logar    
    elif(opcaoMenu == 2):


    #Alterar produto
    elif(opcaoMenu == 3):


    #Deletar produto 
    elif(opcaoMenu == 4):

    
    #Sair
    elif(opcaoMenu == 5):
        print("Voçe desejou sair do programa, Até mais")
        break
    
    else:
        print("Opção invalida!! TENTE NOVAMENTE ")
    






















#Chamando o procedimento da tabela estado
tabelaEstado.tabela_estado
#tabelaEstado.inserir_dados

#Chamando o procedimento da tabela cidade
tabelaCidade.tabela_cidade
#tabelaCidade.Inserir_dados

#Chamando o procedimento  da tabela cliente
tabelaCliente.tabela_cliente
#tabelaCliente.Inserir_dados

#Chamando o procedimento da tabela transporte
tabelaTransporte.tabela_transporte
#tabelaTransporte.Inserir_dados