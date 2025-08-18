# 16/08/2025
# Possui trechos de código de gauss_jordan.py
# Resolve a inversa de uma matriz
# Estou tentando aprimorar a leitura do código e a reutilidade dele em outros, englobando o programa em funções; Primeira tentativa

def criar_matriz_inversa(matriz):
    variaveis = ['x', 'y', 'z', 'a', 'b', 'c']
    linha = 1
    variavel = 0
    while linha <= 3:
        while variavel < 3:
            v = variaveis[variavel]
            c = f"{v}{linha}"
            n = float(input(f"Digite o valor de {c}: "))
            matriz[c] = n
            variavel += 1
        while variavel < 6:
            letra = variaveis[variavel]
            chave = f"{letra}{linha}"
            matriz[chave] = 0
            variavel += 1
        variavel = 0    
        linha += 1
    matriz["a1"] = 1
    matriz["b2"] = 1
    matriz["c3"] = 1
    printar_matriz_inversa(matriz)

def printar_matriz_inversa(matriz):
    linha = 1
    while linha <= 3:
        x = matriz.get('x' + str(linha))
        y = matriz.get('y' + str(linha))
        z = matriz.get('z' + str(linha))
        a = matriz.get('a' + str(linha))
        b = matriz.get('b' + str(linha))
        c = matriz.get('c' + str(linha))
        print(f"| {x} {y} {z} | {a} {b} {c} |")
        linha += 1
    print()    

def resolver_matriz_inversa(matriz):
    variaveis = ['x', 'y', 'z', 'a', 'b', 'c']
    variavel = 0
    linha = 1
    passo = 1
    num_var = len(variaveis)

    # Gauss-Jordan
    while linha <= 3:
        elemento = f'{variaveis[variavel]}{linha}'
        valor_elemento = matriz.get(elemento)
        # Transformar linha para que elemento vire '1'
        if valor_elemento != 1 and valor_elemento != 0:
            i = variavel
            while i < num_var:
                chave = f'{variaveis[i]}{linha}'
                valor = matriz.get(chave)
                matriz[chave] = valor / valor_elemento
                if matriz[chave] != 1 and i == variavel:
                    exit()
                
                i += 1
            print(f"Passo {passo}:")
            printar_matriz_inversa(matriz)
            passo += 1
            print(f"{elemento} Igualado a 1")
            print()
        elif valor_elemento == 0: # Procurar troca de linhas
            i = linha
            if i < 3:
                while i < 3:
                    chave = f'{variaveis[variavel]}{i + 1}'
                    valor = matriz.get(chave)
                    if valor != 0:
                        j = variavel
                        while j < num_var:
                            chave = f'{variaveis[j]}{i + 1}'
                            valor = matriz.get(chave)
                            chave2 = f'{variaveis[j]}{linha}'
                            valor2 = matriz.get(chave2)
                            matriz[chave] = valor2
                            matriz[chave2] = valor
                            j += 1
                        print(f"Passo {passo}:")
                        printar_matriz_inversa(matriz)
                        passo += 1
                        print(f"Linha {linha} trocada com a linha {i + 1}")
                        print()
                        i = -1
                        break    
                    i += 1
                if i == -1:
                    continue
                else:
                    print("Sistema sem resolucao.")
                    exit()
            else:
                print("Sistema sem resolucao.")
                exit()


        i = linha + 1
        while i <= 3:
            j = variavel
            ref = 0
            while j < num_var: 
                chave = f'{variaveis[j]}{i}'
                valor = matriz.get(chave)
                if j == variavel:
                    ref = valor
                if ref == 0:
                    break
                chave2 = f'{variaveis[j]}{linha}'
                valor2 = matriz.get(chave2)
                matriz[chave] = valor - (ref * valor2)  
                j += 1
            i += 1   
            
        if linha != 3:
            print(f"Passo {passo}:")
            printar_matriz_inversa(matriz)
            print(f"Todos embaixo de {elemento} igualados a 0")
            print()
            passo += 1

        print(f"SAINDO DE {elemento}")
        print()
        variavel += 1
        linha += 1      

    variavel = 2
    linha = 3
    while linha > 1:
        i = linha - 1
        while i >= 1:
            j = variavel
            ref = 0
            while j < num_var:
                chave = f'{variaveis[j]}{i}'
                valor = matriz.get(chave)
                chave2 = f'{variaveis[j]}{linha}'
                valor2 = matriz.get(chave2)
                if j == variavel:
                    ref = valor
                matriz[chave] = valor - (ref * valor2)
                j += 1
            i -= 1        
        print(f"Passo {passo}:")
        printar_matriz_inversa(matriz)
        passo += 1
        variavel -= 1
        linha -= 1

def Matriz_Inversa():
    matriz = {}
    criar_matriz_inversa(matriz)
    return matriz


if __name__ == "__main__":
    matriz = Matriz_Inversa()
    resolver_matriz_inversa(matriz)