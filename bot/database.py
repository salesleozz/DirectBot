import mysql.connector
from instagrapi import Client
from instagrapi.exceptions import ClientError
import time

# Configuração da conexão com o banco de dados
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'insta_leads',
}

# Função para listar tabelas no banco de dados
def list_tables():
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        cursor.close()
        cnx.close()
        return tables
    except Exception as e:
        print(f"Erro ao listar tabelas do banco de dados: {e}")
        return []

# Função para ler os usernames da tabela selecionada
def read_usernames_from_table(table_name):
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = f"SELECT username FROM {table_name}"  # Ajuste se o nome da coluna for diferente
        cursor.execute(query)
        usernames = [row[0] for row in cursor.fetchall()]
        cursor.close()
        cnx.close()
        return usernames
    except Exception as e:
        print(f"Erro ao ler os usernames da tabela {table_name}: {e}")
        return []

def send_direct_message(username, password, recipient_usernames, message, delay=30):
    try:
        client = Client()
        client.login(username, password)
        
        for recipient_username in recipient_usernames:
            if recipient_username:  # Verifique se o nome de usuário não está vazio
                recipient_id = client.user_id_from_username(recipient_username)
                client.direct_send(message, [recipient_id])
                print(f"Mensagem enviada para {recipient_username}: {message}")
                time.sleep(delay)
    except ClientError as e:
        print(f"Erro ao enviar a mensagem: {e}")
