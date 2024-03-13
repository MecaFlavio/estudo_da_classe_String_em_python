# alguns métodos da classe String em python para memorização

curso = "cUrSo de pYtHon"
print(curso.upper()) # texto com letras maiúsculas

print(curso.lower()) #textos com letras minusculas

print(curso.title()) #textos com primeira de cada palavra letra maiúscula

curso= "   Curso de Python   "

print(curso.strip()) # elimina espaço direita e esquerda

print(curso.lstrip()) # elimina espaço esquerda

print(curso.rstrip()) # elimina espaço direita

curso = "Python"

print(curso.center(20, "#")) #centraliza texto acompanhado de um elemento opcional para preencher espaços vazios

print(".".join(curso)) #intercala o simbolo indicado entre os caracteres da string passada na instrução do método

print(" ".join(curso.center(10, "#"))) # exemplo juntando os dois métodos

# INTERPOLAÇÃO DE STRINGS

nome = "Flávio"
idade = 34
profissao = "Programador"
linguagem = "Python"

# Jeito antigo
print ("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# Metodo format()
print ("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem))

# fstring
print (f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# formatação

PI = 3.14159
print(f"Valor de PI é: {PI:2f}")
print(f"Valor de PI é: {PI:10.2f}")

# Fatiamento de String

nome = "Flávio Alves Pereira"

print(nome[0])

print(nome[-1])

print(nome[:9])

print(nome[10:])

print(nome[10:20])

print(nome[10:20:2])

print(nome[:])

print(nome[::-1])

# String de Múltiplas linhas

nome = "Flávio"

mensagem = f"""
  Olá meu nome é {nome},
Eu estou aprendendo Python.
   Essa mensagem tem diferentes recuos"""

print(mensagem)