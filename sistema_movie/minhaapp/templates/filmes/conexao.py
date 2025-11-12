import mysql.connector
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host = 'localhost',
            user ='root',
            password = 'Aluno',
            database = 'senabet'
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        print("Não foi possível conectar ao Mysql", e)
        return None

