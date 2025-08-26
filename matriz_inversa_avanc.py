# matriz_inversa_2.py
# 18/08/2025

"""
Apenas matrizes quadradas podem ser invertidas.
Além disso, para que uma matriz quadrada seja inversível, seu determinante deve ser diferente de zero.
Uma matriz que não pode ser invertida é chamada de matriz singular. Isso significa que ela não possui uma matriz inversa multiplicativa.
"""
from matriz import criar_matriz
from determinante import achar_determinante
from gauss_jordan_avanc import resolver_gauss_jordan

def criar_matriz_inversa(m):
    dimensao = m.linhas
    colunas = m.colunas
    if dimensao != colunas:
        print("Essa matriz nao e quadrada, portanto ela e singular e nao tem inversa.")
        exit()
    if achar_determinante(m) == 0:
        print("Essa matriz possui determinante igual a 0, portanto ela e singular e nao tem inversa.")
        exit()
    m.colunas = colunas * 2
    linha = 1
    e = m.elementos    
    while linha <= dimensao:
        j = colunas + 1
        while j <= m.colunas:
            chave = f"a{linha}{j}"
            if linha + dimensao == j:
                e[chave] = 1
            else:    
                e[chave] = 0 
            j += 1       
        linha += 1
    printar_matriz_inversa(m)
    return m



def printar_matriz_inversa(matriz):
    m = matriz.elementos
    #num_restantes = m.copy()
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
                #num_restantes.pop(num)
                if c == colunas // 2:
                    linha += ' |'
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

def desfazer_matriz_inversa(matriz):
    m = matriz.elementos
    m_copia = {}

    for num in m:
        aij = list(num)
        if int(aij[2]) > matriz.colunas // 2:
            m_copia[f'a{aij[1]}{int(aij[2]) - matriz.colunas // 2}'] = m.get(num)
    matriz.elementos = m_copia        



def Matriz_Inversa(m):
    matriz = criar_matriz_inversa(m)
    resolver_gauss_jordan(matriz, matriz.colunas // 2)
    desfazer_matriz_inversa(matriz)
    return matriz

def main():
    m = criar_matriz()
    matriz = criar_matriz_inversa(m)
    resolver_gauss_jordan(matriz, matriz.colunas // 2)
    return m

if __name__ == "__main__":
    main()
    