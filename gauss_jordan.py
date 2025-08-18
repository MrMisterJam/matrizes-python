sistema = {}
variaveis = ['x', 'y', 'z', 'a']
linha = 1
variavel = 0

while linha <= 3:
    while variavel < 4:
        v = variaveis[variavel]
        c = f"{v}{linha}"
        n = float(input(f"Digite o valor de {c}: "))
        sistema[c] = n
        variavel += 1
    variavel = 0    
    linha += 1



def printar_sistema(sistema):
    linha = 1
    while linha <= 3:
        x = sistema.get('x' + str(linha))
        y = sistema.get('y' + str(linha))
        z = sistema.get('z' + str(linha))
        a = sistema.get('a' + str(linha))
        print(f"L{linha}: {x}x + {y}y + {z}z = {a}")
        linha += 1

printar_sistema(sistema)
print()

def resolver_sistema(sistema):
    
    variaveis = ['x', 'y', 'z', 'a']
    variavel = 0
    linha = 1
    passo = 1

    while linha <= 3:
        var_nome = f'{variaveis[variavel]}{linha}'
        var_valor = sistema.get(var_nome)
        
        if var_valor != 1 and var_valor != 0:
            i = variavel
            while i < 4:
                chave = f'{variaveis[i]}{linha}'
                valor = sistema.get(chave)
                sistema[chave] = valor / var_valor
                if sistema[chave] != 1 and i == variavel:
                    exit()
                
                i += 1
            print(f"Passo {passo}:")
            printar_sistema(sistema)
            print()
            passo += 1
            print(f"{var_nome} Igualado a 1")
            print()
        elif var_valor == 0:
            i = linha
            if i < 3:
                while i < 3:
                    chave = f'{variaveis[variavel]}{i + 1}'
                    valor = sistema.get(chave)
                    if valor != 0:
                        j = variavel
                        while j < 4:
                            chave = f'{variaveis[j]}{i + 1}'
                            valor = sistema.get(chave)
                            chave2 = f'{variaveis[j]}{linha}'
                            valor2 = sistema.get(chave2)
                            sistema[chave] = valor2
                            sistema[chave2] = valor
                            j += 1
                        print(f"Passo {passo}:")
                        printar_sistema(sistema)
                        print()
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
            while j < 4: 
                chave = f'{variaveis[j]}{i}'
                valor = sistema.get(chave)
                if j == variavel:
                    ref = valor
                if ref == 0:
                    break
                chave2 = f'{variaveis[j]}{linha}'
                valor2 = sistema.get(chave2)
                sistema[chave] = valor - (ref * valor2)  
                j += 1
            i += 1   
            
        if linha != 3:
            print(f"Passo {passo}:")
            printar_sistema(sistema)
            print()
            print(f"Todos embaixo de {var_nome} igualados a 0")
            print()
            passo += 1

        print(f"SAINDO DE {var_nome}")
        print()
        variavel += 1
        linha += 1      

    variavel = 2
    linha = 3
    while linha > 1:
        i = linha - 1
        while i >= 1:
            j = variavel
            ref = 1
            while j < 4:
                chave = f'{variaveis[j]}{i}'
                valor = sistema.get(chave)
                chave2 = f'{variaveis[j]}{linha}'
                valor2 = sistema.get(chave2)
                if j == variavel:
                    ref = valor
                sistema[chave] = valor - (ref * valor2)
                j += 1
            i -= 1        
        print(f"Passo {passo}:")
        printar_sistema(sistema)
        print()
        passo += 1
        variavel -= 1
        linha -= 1 
    
    print(f"| x = {sistema.get('a1')}")
    print(f"| y = {sistema.get('a2')}")
    print(f"| z = {sistema.get('a3')}")  
    print()  

resolver_sistema(sistema)