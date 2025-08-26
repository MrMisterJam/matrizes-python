# transposta.py

from matriz import instanciar_matriz, criar_matriz, printar_matriz

def transpor_matriz(matriz):
    m = matriz.elementos
    linhas = matriz.linhas
    colunas = matriz.colunas
    matriz_transposta = {}

    j = 1
    while j <= colunas:
        i = 1
        while i <= linhas:
            a = f'a{j}{i}'
            matriz_transposta[a] = m.get(f'a{i}{j}')
            i += 1
        j += 1 
    return instanciar_matriz(matriz_transposta, colunas, linhas)

def Transposta():
    matriz = criar_matriz()
    matriz = transpor_matriz(matriz)
    printar_matriz(matriz)

if __name__ == '__main__':
    Transposta()    