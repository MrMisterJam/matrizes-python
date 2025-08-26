# determinante.py
# 16/08/2025

"""
O determinante de uma matriz só pode ser calculado se a matriz for quadrada.
Se uma matriz tiver uma linha ou coluna de zeros, seu determinante será zero. 
O determinante pode ser usado para verificar se uma matriz é invertível (se o determinante é diferente de zero). 

Sarrus é bem mais eficiente que sarrus2 nesse caso; porém, sarrus2 foi um exercício prático de escalabilidade.
"""

from matriz import criar_matriz, instanciar_matriz



def achar_determinante(matriz):
    linhas = matriz.linhas
    colunas = matriz.colunas
    resultado = 0
    if linhas != colunas:
        print("Essa matriz nao possui determinante.")
        exit()
    if linhas == 1:
        resultado = matriz.elementos.get('a11')
    elif linhas == 2:
        resultado = determinante_2x2(matriz)
    elif linhas == 3:
        resultado = sarrus(matriz)
    else:
        resultado = laplace(matriz)        


    return resultado    



def determinante_2x2(matriz):
    valor1 = matriz.elementos.get("a11") * matriz.elementos.get("a22")
    valor2 = matriz.elementos.get("a12") * matriz.elementos.get("a21")
    resultado = valor1 - valor2
    return resultado

def sarrus(matriz):
    m = matriz.elementos
    a11 = m.get("a11")
    a12 = m.get("a12")
    a13 = m.get("a13")
    a21 = m.get("a21")
    a22 = m.get("a22")
    a23 = m.get("a23")
    a31 = m.get("a31")
    a32 = m.get("a32")
    a33 = m.get("a33")
    resultado = (a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32) - (a13 * a22 * a31) - (a11 * a23 * a32) - (a12 * a21 * a33)
    return resultado

def sarrus2(matriz):
    m = matriz.elementos
    dic = {
        '1': 1,
        '2': 2,
        '3': 3
    }
    i = 0
    soma = 0
    while i < 3:
        j = 1
        produto = 1
        while j <= 3:
            k = dic.get(str(j))
            e = f'a{j}{k}'
            valor = m.get(e)
            produto *= valor
            if k < 3:
                dic[str(j)] = k + 1
            else:
                dic[str(j)] = 1 
            j += 1
        soma += produto
        i += 1
    i = 0    
    subtracao = 0
    dic['1'] = 3
    dic['2'] = 2
    dic['3'] = 1
    while i < 3:
        j = 1
        produto = 1
        while j <= 3:
            k = dic.get(str(j))
            e = f'a{j}{k}'
            valor = m.get(e)
            produto *= valor
            if k < 3:
                dic[str(j)] = k + 1
            else:
                dic[str(j)] = 1 
            j += 1
        subtracao += produto
        i += 1    
    resultado = soma - subtracao
    return resultado

def laplace(matriz):
    m = matriz.elementos
    linhas = matriz.linhas
    colunas = matriz.colunas
    j = 1
    soma = 0
    while j <= colunas:
        num = m.get(f'a1{j}')
        if num == 0:
            j += 1
            continue
        matriz_resultante = {}
        mri = 1
        mrj = 1
        for e in m:
            aij = list(e)
            ai = int(aij[1])
            aj = int(aij[2])
            if ai != 1 and aj != j:
                matriz_resultante[f'a{mri}{mrj}'] = m.get(e)
                if mrj == colunas - 1:
                    mrj = 1
                    mri += 1
                else:
                    mrj += 1       
        obj = instanciar_matriz(matriz_resultante, linhas - 1, colunas - 1)     
        det = achar_determinante(obj)    
        cofator = pow(-1, 1 + j) * det
        soma += num * cofator
        j += 1
    return soma    

if __name__ == "__main__":

    matriz = criar_matriz()
    print(f'Determinante = {achar_determinante(matriz)}')