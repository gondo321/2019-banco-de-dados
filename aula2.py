import sqlite3


# Importa a biblioteca do sqlite para usar o banco
import sqlite3

# Procedimento que recebe uma conexão e cria uma tabela


def criar_tabela_usuario(conexao):

    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()

    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS usuario (
                nome TEXT NOT NULL,
                login TEXT NOT NULL,
                senha TEXT NOT NULL
            ); '''

    # Executa o SQL
    cursor.execute(sql)

# Procedimento que recebe a conexão


def inserir_usuario(conexao):
    # Cria o cursor
    nome = input("Insira seu nome: ")
    login = input("Insira o login: ")
    senha = input("Insira a senha: ")
    cursor = conexao.cursor()
    # Monta o SQL
    sql = '''
        INSERT INTO usuario VALUES(
            '{}',
            '{}',
            '{}'
        );
    ''' .format(nome, login, senha)
    # Executa
    cursor.execute(sql)
    # Quanto insere, altera ou exclui tem que fazer o commit
    # Que é como se fosse um "salvar" para registrar as alterações feitas
    conexao.commit()

def listar_usuarios(conexao):
    cursor = conexao.cursor()
    
    sql = '''
        select rowid, * from usuario;

    '''
    cursor.execute(sql)

    lista = cursor.fetchall()
    
    print(lista)
    print("ID\t Nome\t Login\t")
    

    for u in lista:
        print("{}\t {}\t {}".format(u[0], u[1], u[2]))
        


################################
###### Programa principal ######
################################

# Cria a conexão com o banco de dados
conexao = sqlite3.connect("banco.sqlite")



# Executa o procedimento
#criar_tabela_usuario(conexao)

# Executa o procedimento
#inserir_usuario(conexao)

# listar usuario

listar_usuarios(conexao)
# Fecha a conexão
conexao.close()
