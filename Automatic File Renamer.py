import os

# Caminho da pasta
pasta = r"C:\Users\YourName\OneDrive\Pictures\Screenshots"
# Prefixo do nome dos arquivos
prefixo = "foto"

# Contador
contador = 1

for arquivo in os.listdir(pasta):
    caminho_antigo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_antigo):
        extensao = os.path.splitext(arquivo)[1]
        novo_nome = f"{prefixo}_{contador}{extensao}"
        caminho_novo = os.path.join(pasta, novo_nome)

        os.rename(caminho_antigo, caminho_novo)

        print(f"{arquivo} → {novo_nome}")
        contador += 1