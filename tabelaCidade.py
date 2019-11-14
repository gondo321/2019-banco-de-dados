#Importar biblioteoca
import sqlite3


# Criação da tabela cidade
def tabela_cidade(conexao):
    cursor = conexao.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS cidade,
        nome TEXT NOT NULL,
        idest INTEGER NOT NULL,
        FOREIGN KEY(idest) REFERENCES estado(rowid)

        );'''
    
    cursor.execute(sql)


#Inserir dados na tabela cidade
def Inserir_dados(conexao):
    nome = input("Nome da cidade: ")

    cursor = conexao.cursor()

    sql = '''
        INSERT INTO cidade VALUES(

            '{}'
        );
        '''.format(nome)
    cursor.execute(sql)

    #commit para salvar
    conexao.commit()


    

    
