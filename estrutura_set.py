# Conjuntos Python - SET

print(set([1,2,1,2,3,4]))
print(set("abacaxi"))
print(set(("palio", "fiat", "celta", "palio")))

numeros = {1, 2, 3, 4}
numeros = list(numeros)
print(numeros[0])

carro = {"palio", "fiat", "celta", "palio"}
for indice, carro in enumerate(carro):
    print(indice , carro)

# union()
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a)
print(conjunto_a.union(conjunto_b))

# intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.intersection(conjunto_b))

# diference
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# symmetric_diference
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_b.symmetric_difference(conjunto_a))

# issubjset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

# superset
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

# isdisjoint
conjunto_a = {1, 2, 3}
conjunto_b = {7, 4, 8, 6, 9}
conjunto_c = {1, 0}
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

# add()

sorteio = {1, 23}
print(sorteio.add(25))
print(sorteio.add(42))
print(sorteio.add(1))

# clear
sorteio.clear()
print(sorteio)

#copy()

conjunto_c = conjunto_b.copy()
print(conjunto_c)

# discard()

conjunto_c.discard(4)
print(conjunto_c)

# pop
conjunto_c.pop()
print(conjunto_c)

# remove()
conjunto_c.remove(9)
print(conjunto_c)

# len
print(len(conjunto_c))

# on
print(1 in conjunto_c)
print(7 in conjunto_c)