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