from ftplib import FTP
import json

# Configuração do servidor FTP
FTP_HOST = "10.10.0.23"
FTP_PORT = 21  # Porta padrão do FTP
FTP_USER = "ftp-users"  # Troque se precisar
FTP_PASS = "Password546"  # Normalmente vazio para usuários anônimos

try:
    # Conectar ao servidor FTP
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
