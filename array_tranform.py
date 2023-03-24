def ler_dominios(arquivo):
    with open(arquivo, 'r') as f:
        dominios = [linha.strip() for linha in f.readlines()]
    return dominios

arquivo_dominios = 'pesoreal.xyz.txt' 
dominios = ler_dominios(arquivo_dominios)
print(dominios)