# matriz.py
import math

class _Matriz:
    def __init__(self, matriz, linhas, colunas):
        self.elementos = matriz
        self.linhas = linhas
        self.colunas = colunas



def criar_matriz():
    matriz = {}
    linhas = int(input("Quantas linhas tem a matriz? "))
    colunas = int(input("Quantas colunas tem a matriz? "))
    print()
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
    print()
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
    obj = _Matriz(matriz, linhas, colunas)    
    printar_matriz(obj)
    return obj     

def instanciar_matriz(elementos, linhas, colunas):
    return _Matriz(elementos, linhas, colunas)

def printar_matriz(matriz):
    m = matriz.elementos
    colunas = matriz.colunas
    linhas = matriz.linhas
    c = 1
    linha = '| '
    i = 1
    while i <= linhas:
        for num in m:
            aij = list(num)
            if int(aij[1]) == i:
                linha += str(m.get(num))
                if c == colunas:
                    linha += ' |'
                else:
                    linha += '  '
                    c += 1
        print(linha)            
        c = 1
        linha = '| '
        i += 1 
    print()      

def singular(matriz):
    from determinante import achar_determinante
    return bool(achar_determinante(matriz))

def frobenius(matriz):
    m = matriz.elementos
    soma = 0
    for num in m:
        soma += pow(m.get(num), 2)
    print(f'Soma = {soma}')    
    return math.sqrt(soma)    

def numero_de_condicao(matriz):
    from matriz_inversa_avanc import Matriz_Inversa
    return frobenius(matriz) * frobenius(Matriz_Inversa(matriz))