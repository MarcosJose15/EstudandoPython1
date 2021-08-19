"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas
For(para), in(detro)

C ou Java

for(int i = 0; i < 10; i++){
   //execução do loop
}

Python

for item in interavel:
   //execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)
    print('\n')

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)
    print('\n')


# Exemplo de for 3 (iterando sobre um range)
"""
range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não
"""
for numero in range(1,10):
    print(numero)
    print('\n')



nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

"""
Enumerate:
((0, 'G')m (1, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)
"""
for indice, letra in enumerate(nome):
    print(nome[indice])

for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor[0])

for valor in enumerate(nome):
    print(valor[1])