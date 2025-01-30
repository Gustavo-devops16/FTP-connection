from ftplib import FTP
import json

# Configuração do servidor FTP
FTP_HOST = "" #seu ip
FTP_PORT = 21  
FTP_USER = "" # user configurado no server  
FTP_PASS = ""  # senha do user

try:
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT, timeout=10)  # Conecta ao servidor
    ftp.login(FTP_USER, FTP_PASS)  # Faz login
    print(f"Conectado ao FTP: {FTP_HOST}")

    # Listar arquivos do diretório raiz
    print("Listando arquivos e diretórios:")
    ftp.retrlines("LIST")

    # Fechar conexão
    ftp.quit()
    print("Conexão encerrada.")

except Exception as e:
    print(f"Erro ao conectar: {e}")
