import mysql.connector

def criar_db():
    try: 
        mydb = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='banco'
        )
    except Exception as ex:
        print(f"Ocorreu erro na conexão com o Banco de dados: {ex}")

    return mydb