# Programar baseado em funções torna o código mais legível e possibilita 
# o reaproveitamento do código. Programar baseado em funções torna, é o 
# mesmo que dizer que estamos programando de forma estruturada.

# Exemplos
def exibir_mensagem():
    print("Olá Mundo")

def exibir_mensagem2(nome):
    print(f"Seja Bem Vindo {nome}")

def exibir_mensagem3(nome="Anonimo"):
    print(f"Seja bem Vindo {nome}")

exibir_mensagem()
exibir_mensagem2(nome="Flavio")
exibir_mensagem3()
exibir_mensagem3(nome="Ana")

# Para retornar um valor, utilizamos a palavra reservada return 
# Toda função Python retorna NONE por padrão.
# Em Python, uma função pode retornar mais de um valor

# exemplo

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Tem que retornar NONE")
    # return none

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3())

# Argumentos Nomeados

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# salvar_carro(marca="Fiat", modelo="Palio",ano=1999, placa="ABC-1234")
# salvar_carro(**{"marca": "Fiat", "modelo":"Palio", "Ano": 1999, "Placa": "ABC-1234"})

# Args e Kwargs
# Podemos combinar parâmetros obrigatórios com arg e kwargs.
# Quando esses são definidos (*args e **kwargs), o método recebe
# os valores como tupla e dicionário respectivamente

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados="\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema("18 de Agosto de 2024", "Zen of Python", "Beautiful is better than ugly","Explicit is better than implicit", autor="Tim Peters", ano=1999, aka="O brabo")

