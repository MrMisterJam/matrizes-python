class _Matriz:
    def __init__(self, matriz, linhas, colunas):
        self.elementos = matriz
        self.linhas = linhas
        self.colunas = colunas



def criar_matriz():
    matriz = {}
    linhas = int(input("Quantas linhas tem a matriz? "))
    colunas = int(input("Quantas colunas tem a matriz? "))
    i = 1
    while i <= linhas:
        j = 1
        while j <= colunas:
            elemento = f'a{i}{j}'
            n = input(f"Digite o valor de {elemento}: ")
            try:
                matriz[elemento] = float(n)
            except:
                matriz[elemento] = n
            j += 1
        j = 1
        i += 1
    obj = _Matriz(matriz, linhas, colunas)      
    printar_matriz(obj)
    return obj 

def digitar_matriz(linhas, colunas):
    matriz = {}
    i = 1
    while i <= linhas:
        j = 1
        while j <= colunas:
            elemento = f'a{i}{j}'
            n = input(f"Digite o valor de {elemento}: ")
            try:
                matriz[elemento] = float(n)
            except:
                matriz[elemento] = n
            j += 1
        j = 1
        i += 1
    printar_matriz(matriz, colunas)
    return matriz     

def printar_matriz(m):
    matriz = m.elementos
    colunas = m.colunas
    c = 1
    linha = '| '
    for num in matriz:
        linha = linha + str(matriz.get(num))
        if c == colunas:
            linha = linha + ' |'
            print(linha)
            linha = '| '
            c = 1
        else:
            linha = linha + '   '
            c += 1
