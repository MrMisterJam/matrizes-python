# gauss_jordan_avanc.py
# 18/08/2025

from matriz import digitar_matriz, printar_matriz

def resolver_gauss_jordan(matriz, var):
    m = matriz.elementos
    linhas = matriz.linhas # Operações
    colunas = matriz.colunas
    passo = 1
    linha = 1
    coluna = 1
    repeticoes = min(colunas, var)
    while linha <= repeticoes:
        var_nome = f'a{linha}{coluna}'
        var_valor = m.get(var_nome)
        
        if var_valor != 1 and var_valor != 0:
            j = coluna
            while j <= colunas:
                ele = f'a{linha}{j}'
                valor = m.get(ele)
                m[ele] = valor / var_valor
                if m[ele] != 1 and j == coluna:
                    exit()
                j += 1
            print(f"Passo {passo}:")
            printar_matriz(matriz)
            passo += 1
            print(f"Pivo da coluna {coluna} dividindo a linha {linha} por {var_valor}.")
            print()
        elif var_valor == 0:
            i = linha
            if i < linhas:
                while i < linhas:
                    chave = f'a{i + 1}{coluna}'
                    valor = m.get(chave)
                    if valor != 0:
                        j = coluna
                        while j < colunas:
                            chave = f'a{i + 1}{j}'
                            valor = m.get(chave)
                            chave2 = f'a{linha}{j}'
                            valor2 = m.get(chave2)
                            m[chave] = valor2
                            m[chave2] = valor
                            j += 1
                        print(f"Passo {passo}:")
                        printar_matriz(matriz)
                        passo += 1
                        print(f"Linha {linha} trocada com a linha {i + 1}")
                        print()
                        j = -1
                        break    
                    i += 1
                if j == -1:
                    continue
                else:
                    print("Sistema sem resolucao.")
                    exit()
            else:
                print("Sistema sem resolucao.")
                exit()


        i = linha + 1
        while i <= linhas:
            j = coluna
            ref = 0
            while j <= colunas: 
                chave = f'a{i}{j}'
                valor = m.get(chave)
                if j == coluna:
                    ref = valor
                if ref == 0:
                    break
                chave2 = f'a{linha}{j}'
                valor2 = m.get(chave2)
                m[chave] = valor - (ref * valor2)  
                j += 1
            i += 1   
            
        if linha != linhas:
            print(f"Passo {passo}:")
            printar_matriz(matriz)
            print(f"Todos embaixo de {var_nome} eliminados.")
            print()
            passo += 1

        print(f"Seguindo de {var_nome}")
        print()
        coluna += 1
        linha += 1      

    coluna = repeticoes
    linha = repeticoes
    while linha > 1:
        i = linha - 1
        while i >= 1:
            j = coluna
            ref = 1
            while j <= colunas:
                chave = f'a{i}{j}'
                valor = m.get(chave)
                chave2 = f'a{linha}{j}'
                valor2 = m.get(chave2)
                if j == coluna:
                    ref = valor
                m[chave] = valor - (ref * valor2)
                j += 1
            i -= 1        
        print(f"Passo {passo}:")
        printar_matriz(matriz)
        print(f"Coluna {coluna} eliminada.")
        print()
        passo += 1
        coluna -= 1
        linha -= 1   
    
    

def gauss_jordan():
    v = int(input("Quantas variaveis tem? "))
    o = int(input("Quantas operacoes tem? "))
    matriz = digitar_matriz(o, v + 1)
    resolver_gauss_jordan(matriz, v)

if __name__ == '__main__':
    gauss_jordan()    