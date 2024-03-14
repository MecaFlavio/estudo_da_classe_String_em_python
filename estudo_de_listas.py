print("Criação de listas".center(26,"#"))
frutas = ["Laranja", "Maça", "Uva", "pera"]

fruta = []

letras = list("paralelepipedo")

numeros = list(range(10))

carro = ["Ferrari", "F8", 12000.5, 2020, 2900, "São Paulo", True]

print(frutas)
print(fruta)
print(letras)
print(numeros)
print(carro)

print("Acessando itens da lista".center(26,"#"))
print(frutas[2])
print(frutas[-1])

# lista aninhada
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print("Acesso da lista aninhada".center(26,"#"))
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

print("fatiando uma lista".center(26,"#"))
print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:14:2])
print(letras[:])
print(letras[::-1])

# Iteração
for numero in numeros:
    print(numero)

# Enumerando os items
for indice, item in enumerate(carro):
    print(f"Indice {indice}, Item {item}")

# manipulando lista 
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
print(pares)

# compreention

impar = [numero for numero in numeros if numero % 2 == 1]

print(impar)

quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

quadrado = [numero **2 for numero in numeros]

print(quadrado)