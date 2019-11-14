# importar biblioteca
import sqlite3

#Criação da tabela
def tabela_transporte(conexao):
    cursor = conexao.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS transporte,
        descricao TEXT NOT NULL,
        cidOrig INTEGER NOT NULL,
        cidDest INTEGER NOT NULL,
        idcli INTEGER NOT NULL,
        FOREING KEY(cidOrig) REFERENCES cidade(rowid),
        FOREING KEY(cidDest) REFERENCES cidade(rowid),
        FOREING KEY(idcli) REFERENCES cliente(rowid)
    ); '''

    cursor.execute(sql)


#Inserir dados
def Inserir_dados(conexao):
    cid_Orig = input("Digite a cidade Origem: ")
    cid_dest = input("Digite sua cidade de destino:  ")
    descricao = input("Digite a descrição do produto: ")


    cursor = conexao.cursor()

    sql = '''
        INSERT INTO transporte VALUES(
            '{}'
            '{}'
            '{}'
        );
        '''.format(cid_Orig,cid_dest,descricao)

    cursor.execute(sql)

    #Commit para salvar
    conexao.commit()

#Alterar produto
def alterar_produto(conexao):
    cursor = conexao.cursor()

    sql = '''
        ALTER TABLE transporte

    '''
    
