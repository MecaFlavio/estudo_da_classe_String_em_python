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
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

# comprehennsion

impar = [numero for numero in numeros if numero % 2 == 1]

print(impar)

quadrado = [numero **2 for numero in numeros]

print(quadrado)

# Métodos da classe Lista

# append()
lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,20])
lista.append("Python")

print(lista)

# copy()

lista2 = lista.copy()

print(lista)
print(lista2)

# clear()

lista.clear()

print(lista)
print(lista2)

# count()

print(lista2.count("Python"))

# extend()

n1 = [1, 2, 2, 3]
n2 = [4, 5, 5, 6]

n1.extend(n2)

print(n1)
print(n2)

# index()

print(n1.index(2))

# pop()

n1.pop()

print(n1)

n1.pop(1)

print(n1)

# remove()

n1.remove(5)

print(n1)

# reverse()

n1.reverse()
print(n1)

# sort()

nomes = ["Flavio", "Alan", "Paulo", "Joao", "Camila"]
print(nomes)
nomes.sort()
print(nomes)

nomes.sort(reverse=True)
print(nomes)

nomes.sort(key=lambda x: len(x))
print(nomes)

nomes.sort(key=lambda x: len(x), reverse=True)
print(nomes)

# len()

print(len(nomes))

# sorted()

print(sorted(nomes))

n3 = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(n3)






