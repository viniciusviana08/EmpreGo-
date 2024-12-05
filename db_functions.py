import mysql.connector
from config import *

#Estabelece conexão com o BD
def conectar_db():
    conexao = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
    )
    # altera o cursor para dicionário
    cursor = conexao.cursor(dictionary=True)
    return conexao, cursor

# Encerra a conexão com BD
def encerrar_db(cursor, conexao):
    cursor.close()
    conexao.close()

def limpar_input(campo):
    campolimpo = campo.replace(".","").replace("/","").replace("-","").replace(" ","").replace("(", "").replace(")","").replace("R$","")
    return campolimpo
