# determinante_gauss.py
# 25/08/2025

from matriz import criar_matriz, printar_matriz

def executar_gauss(matriz):
    m = matriz.elementos
    linhas = matriz.linhas
    colunas = matriz.colunas
    sinal = 1
    determinante = 1
    linha = 1
    coluna = 1
    while linha < linhas:
        var_nome = f'a{linha}{coluna}'
        var_valor = m.get(var_nome)

        # Condições para troca
        if var_valor < -1 or var_valor > 1 or var_valor == 0:
            i = linha
            j = 0
            if i < linhas:
                while i < linhas:
                    chave = f'a{i + 1}{coluna}'
                    valor = m.get(chave)
                    if valor == 1 or valor == -1:
                        j = coluna
                        while j <= colunas:
                            chave = f'a{i + 1}{j}'
                            valor = m.get(chave)
                            chave2 = f'a{linha}{j}'
                            valor2 = m.get(chave2)
                            m[chave] = valor2
                            m[chave2] = valor
                            j += 1
                        printar_matriz(matriz)
                        j = -1
                        sinal *= -1
                        break    
                    i += 1
                if j == -1:
                    continue
                else:
                    if var_valor == 0:
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
                                    printar_matriz(matriz)
                                    j = -1
                                    sinal *= -1
                                    break    
                                i += 1
                            if j != -1:
                                print("Sistema sem resolucao.")
                                exit()
                        else:
                            print("Sistema sem resolucao.")
                            exit()
            else:
                print("Sistema sem resolucao.")
                exit()
            j = coluna
            var_valor = m.get(var_nome)
            while j <= colunas:
                ele = f'a{linha}{j}'
                valor = m.get(ele)
                m[ele] = valor / var_valor
                j += 1 
            determinante *= var_valor
            printar_matriz(matriz)

        i = linha + 1
        while i <= linhas:
            j = coluna
            ref = 0
            subtrair = False
            while j <= colunas: 
                chave = f'a{i}{j}'
                valor = m.get(chave)
                chave2 = f'a{linha}{j}'
                valor2 = m.get(chave2)
                if j == coluna:
                    ref = valor
                    if ref == 0:
                        break
                    if (ref > 0 and valor2 > 0) or (ref < 0 and valor2 < 0) or (ref < 0 and valor2 > 0):
                        subtrair = True
                if subtrair:
                    m[chave] = valor - (ref * valor2)
                else:
                    m[chave] = valor + (ref * valor2)  
                j += 1
            i += 1
        determinante *= m.get(f'a{linha}{coluna}')
        printar_matriz(matriz)
        coluna += 1           
        linha += 1
    determinante *= m.get(f'a{linha}{coluna}') * sinal
    print(determinante)

if __name__ == "__main__":
    m = criar_matriz()
    executar_gauss(m)    


