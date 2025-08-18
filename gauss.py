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

def resolver_sistema(sistema):
    """
    x1 = sistema.get('x1')
    if x1 == 1:
        print("X1 ja e 1. Prosseguindo...")
    else:
        num = int(input(f"Escreva o num para dividir {x1} para que de 1: "))
        x = x1 * (1 / num)
        if x == 1:
    """

    variaveis = ['x', 'y', 'z', 'a']
    variavel = 0
    linha = 1

    while linha <= 3:
        var_nome = f'{variaveis[variavel]}{linha}'
        var_valor = sistema.get(var_nome)
        #lista_valores = []
        if var_valor != 1:
            i = variavel
            while i < 4:
                chave = f'{variaveis[i]}{linha}'
                valor = sistema.get(chave)
                sistema[chave] = valor / var_valor
                if sistema[chave] != 1 and i == variavel:
                    exit()
                #lista_valores.append(sistema.get(chave))
                i += 1
        """        
        else:
            i = variavel
            while i < 4:
                chave = f'{variaveis[i]}{linha}'
                valor = sistema.get(chave)
                #lista_valores.append(sistema.get(chave))  
                i += 1 
        """            
        i = linha + 1
        while i <= 3:
            j = variavel
            ref = 1
            while j < 4: 
                chave = f'{variaveis[j]}{i}'
                valor = sistema.get(chave)
                chave2 = f'{variaveis[j]}{linha}'
                valor2 = sistema.get(chave2)
                if j == variavel:
                    ref = valor
                #lista_valores.append(sistema.get(chave))
                sistema[chave] = valor - (ref * valor2)  
                j += 1
            i += 1   
        
        print(f"Linha {linha}:")
        printar_sistema(sistema)
        print()
        variavel += 1
        linha += 1      

    """
    x1 = sistema.get('x1')
    if x1 != 1:
        sistema['x1'] = x1 / x1
        y1 = sistema.get('y1')
        sistema['y1'] = y1 / x1

        z1 = sistema.get('z1')
        sistema['z1'] = z1 / x1

        a1 = sistema.get('a1')
        sistema['a1'] = a1 / x1

    x1 = sistema.get('x1')
    y1 = sistema.get('y1')    
    z1 = sistema.get('z1')
    a1 = sistema.get('a1')

    x2 = sistema.get('x2')
    sistema['x2'] = x2 - x2 * x1
    y2 = sistema.get('y2')
    sistema['y2'] = y2 - y2 * y1
    z2 = sistema.get('z2')
    sistema['z2'] = z2 - z2 * z1
    a2 = sistema.get('a2')
    sistema['a2'] = a2 - a2 * a1

    x3 = sistema.get('x3')
    sistema['x3'] = x3 - x3 * x1
    y3 = sistema.get('y3')
    sistema['y3'] = y3 - y3 * y1
    z3 = sistema.get('z3')
    sistema['z3'] = z3 - z3 * z1
    a3 = sistema.get('a3')
    sistema['a3'] = a3 - (a3 * a1)

    y2 = sistema.get('y2')
    if y2 != 1:
        sistema['y2'] = y2 / y2

        z2 = sistema.get('z2')
        sistema['z2'] = z2 / y2

        a2 = sistema.get('a2')
        sistema['a2'] = a2 / y2

    y2 = sistema.get('y2')    
    z2 = sistema.get('z2')
    a2 = sistema.get('a2')    

    y3 = sistema.get('y3')
    sistema['y3'] = y3 - y3 * y2
    z3 = sistema.get('z3')
    sistema['z3'] = z3 - z3 * z2
    a3 = sistema.get('a3')
    sistema['a3'] = a3 - (a3 * a2)

    z3 = sistema.get('z3')
    if z3 != 1:
        sistema['z3'] = z3 / z3
        
        a3 = sistema.get('a3')
        sistema['a3'] = a3 / z3
    """    
        

resolver_sistema(sistema)        

