import json
from ftplib import FTP
import time
from datetime import datetime

# Configuração do servidor FTP
FTP_HOST = "10.10.0.23"
FTP_PORT = 21  # Porta padrão do FTP
FTP_USER = "ftp-users"  # Troque se precisar
FTP_PASS = "Password546"  # Normalmente vazio para usuários anônimos

# Função para estabelecer a conexão com o FTP
def connect_ftp():
    try:
        ftp = FTP()
        ftp.connect(FTP_HOST, FTP_PORT, timeout=10)
        ftp.login(FTP_USER, FTP_PASS)
        print(f"Establishing connection with the FTP server: {FTP_HOST}")
        return ftp
    except Exception as e:
        print(f"Error connecting to FTP: {e}")
        return None

# Função para listar arquivos e diretórios no FTP
def list_ftp(ftp):
    try:
        if ftp:  # Verificar se a conexão foi bem-sucedida
            print("Files and directories:")
            ftp.retrlines("LIST")
        else:
            print("invalid connection!")
    except Exception as e:
        print(f"Error listing directories: {e}")

# Função para baixar o arquivo venda.json do FTP
def download_json(ftp):
    try:
        if ftp:  # Verificar se a conexão foi bem-sucedida
            # Verificar se o arquivo venda.json existe no FTP
            files = ftp.nlst()  # Lista os arquivos no diretório atual
            if "venda.json" in files:
                # Baixar o arquivo venda.json para o diretório local
                with open("venda.json", "wb") as local_file:
                    ftp.retrbinary("RETR venda.json", local_file.write)
                print("Arquivo venda.json baixado com sucesso.")
                
                # Ler e retornar os dados do arquivo JSON
                with open("venda.json", "r") as json_file:
                    sale_data = json.load(json_file)
                return sale_data
            else:
                print("Arquivo venda.json não encontrado no FTP.")
                return None
        else:
            print("Conexão FTP inválida!")
            return None
    except Exception as e:
        print(f"Erro ao baixar o arquivo venda.json: {e}")
        return None

# Função para chamar as funções de conexão e listagem em um horário específico
def schedule(target_hour, target_minute):
    while True:
        current_time = datetime.now()
        
        # Verificar se é o horário específico
        if current_time.hour == target_hour and current_time.minute == target_minute:
            print("Starting execution")

            # Conectar ao FTP
            ftp = connect_ftp()
            if ftp:
                # Listar diretórios e arquivos
                list_ftp(ftp)
                
                # Baixar o arquivo venda.json
                sale_data = download_json(ftp)
                if sale_data:
                    print("Dados do arquivo venda.json:", sale_data)
                else:
                    print("Falha ao processar o arquivo venda.json.")
                
                ftp.quit()
                print("Conexão terminada.")
            else:
                print("Falha na conexão com o FTP.")

        
            time.sleep(60)
        else:
            
            time.sleep(30)

#verifies the ftp at a especific time
schedule(12, 2)
