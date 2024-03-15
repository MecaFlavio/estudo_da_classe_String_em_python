#criando um dicionário

pessoa = {"nome": "Flavio", "Idade": 28}

pessoa = dict(nome="Flavio", idade=28 )

pessoa["telefone"] = "3333-3333"

print(pessoa)

# acessando valores no dicionário

print(pessoa["nome"])

# alterando valores

pessoa["nome"] = "Maria"
print(pessoa)

# Estruturas aninhadas

contatos = {
    "marta@hotmail.com": {"nome": "marta", "idade": 34},
    "flavio@gmail.com": {"nome": "flavio", "idade": 35},
    "joao@yahoo.com": {"nome": "joao", "idade": 23},
    "maria@hotmail.com": {"nome": "maria", "idade": 45},
}

# acessando dicionários aninhados

print(contatos ["joao@yahoo.com"]["idade"])

#iteração de um dicionário

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# métodos
    
# copy()
copia = contatos.copy()
print(copia)

# fromkeys()
teste = dict.fromkeys(["nome", "telefone"])
print(teste)

teste2 = dict.fromkeys(["nome", "telefone"], "padrao")
print(teste2)

# get()

print(teste2.get("idade", {}))
print(teste2.get("nome", {}))

# item()

print(teste2.items())

# keys()

print(teste2.keys())

# pop()

print(teste2.pop("nome"))
print(teste2.pop("nome", "chave não encontrada"))

# popitem()

teste2.popitem()
print(teste2)

# 



