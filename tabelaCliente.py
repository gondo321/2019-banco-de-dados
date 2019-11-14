#Importar biblioteca
import sqlite3





#Criação da tabela
def tabela_cliente(conexao):
    cursor = conexao.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS cliente,
        nome TEXT NOT NULL,
        data_nasc DATE NOT NULL,
        cpf TEXT(11) NOT NULL,
        rg TEXT NOT NULL,
        celular TEXT(15) NOT NULL,
        bairro TEXT NOT NULL,
        rua TEXT NOT NULL,
        idcid INTEGER NOT NULL,
        FOREING KEY(idcid) REFERENCES cidade(rowid)
    
    );'''

    cursor.execute(sql)


#Inserir dados
def Inserir_dados(conexao):
    nome = input("Digite seu nome inteiro: ")
    data_nasc = int(input("Insira sua data de nascimento: "))
    cpf = int(input("Insira seu cpf: "))
    rg = int(input("Insira seu Rg: "))
    celular = int(input("Insira seu celular com o DDD: "))
    bairro = int(input("Insira seu bairro: "))
    rua = input("Insira sua rua: ")

    cursor = conexao.cursor()

    sql = '''
        INSERT INTO cliente VALUES(

            '{}'
            '{}'
            '{}'
            '{}'
            '{}'
            '{}'
            '{}'

        );
    '''.format(nome, data_nasc, cpf, rg, celular, bairro, rua)

    cursor.execute(sql)

    #commit para salvar
    conexao.commit()



