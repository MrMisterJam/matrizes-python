"""
n = input("Digite a frase que voce quer que apareca: ")
print(n)



x1 = 0
y1 = 0
z1 = 0
r1 = 0

print(f"{x1}x + {y1}y + {z1}z = {r1}")

o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.
"""
def printar_matriz(matriz, colunas):
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
            





l1 = int(input("Quantas linhas tem a 1a matriz? "))
print(f"A 1a matriz tem {l1} linhas")
c1 = int(input("Quantas colunas tem a 1a matriz? "))
print(f"A 1a matriz tem {c1} colunas")
l2 = int(input("Quantas linhas tem a 2a matriz? "))
print(f"A 2a matriz tem {l2} linhas")
c2 = int(input("Quantas colunas tem a 2a matriz? "))
print(f"A 2a matriz tem {c2} colunas")

if c1 != l2:
    print("ERRO: o num de colunas da primeira matriz deve ser igual ao num de linhas da segunda matriz.")
    exit()

matriz1 = {}
matriz2 = {}

linhasregistradas = 1
colunasregistradas = 1
print("Matriz 1:")
while linhasregistradas <= l1:
    while colunasregistradas <= c1:
        pos = f"{linhasregistradas}{colunasregistradas}"
        n = int(input(f"Digite o num na posicao {pos}: "))
        matriz1[pos] = n
        colunasregistradas += 1
    colunasregistradas = 1    
    linhasregistradas += 1
linhasregistradas = 1    
# print(matriz1)
printar_matriz(matriz1, c1)
print("Matriz 2:")
while linhasregistradas <= l2:
    while colunasregistradas <= c2:
        pos = f"{linhasregistradas}{colunasregistradas}"
        n = int(input(f"Digite o num na posicao {pos}: "))
        matriz2[pos] = n
        colunasregistradas += 1
    colunasregistradas = 1    
    linhasregistradas += 1
# print(matriz2)
printar_matriz(matriz2, c2)
m1l = 1
m1c = 1
m2l = 1
m2c = 1

matriz3 = {}
while m1l <= l1:
    while m2c <= c2:
        xy = 0
        while m1c <= c1:
            x = matriz1.get(f"{m1l}{m1c}")
            y = matriz2.get(f"{m2l}{m2c}")
            xy += x * y
            m1c += 1
            m2l += 1
        matriz3[f"{m1l}{m2c}"] = xy
        m1c = 1
        m2l = 1
        m2c += 1
    m2c = 1    
    m1l += 1
print("Resultado:")
printar_matriz(matriz3, c2)


"""
print(matriz3)

ct3 = c2

c3 = 1
linha = '| '
for num in matriz3:
    linha = linha + str(matriz3.get(num))
    if c3 == ct3:
        linha = linha + ' |'
        print(linha)
        linha = '| '
        c3 = 1
    else:
        linha = linha + '   '
        c3 += 1
"""

