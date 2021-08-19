"""
Tipo sting

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '345', 'a', 'True', '123.5'
- Estiver entre àspas duplas -> "uma string", "345", "a", "True", "123.5"
- Estiver entre àspas simples triplas -> '''uma string''', '''345''', '''a''', '''True''', '''123.5'''
"""
# - Estiver entre àspas duplas triplas -> """uma string""", """345""", """a""", """True""", """123.5"""
"""
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina´s Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) #Transforma em uma lista de strings
"""
nome = "Marcos \" hg"
print(nome)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'
print(nome[0:4])  # Slice de tring

print(nome[5:15])  # Slice de tring

# [ 0,    1]
# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])

nome1 = "LOUCURA TOTAL"
print(nome1.split()[0:14])

print(nome[::-1]) # Inversão de String Pythônico