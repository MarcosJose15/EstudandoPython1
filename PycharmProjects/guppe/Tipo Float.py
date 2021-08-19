"""
Tipo Float
Tipo real, decimal
Casas decimais

OBS: O separador de casas decimais na programação é o ponto e não a vírgula.
"""
# Errado do ponto de vista do Float, mas gera uma tupla (com vírgula)
valor = 1, 44
print(valor)
print(type(valor))

# Certo (com pontos)  
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição na tupla
valor1, valor2 = 1, 44
print(valor1 + valor2)

#Podemos converter um float para um int
"""OBS: Ao converter valores float inteiros, nós perdemos precisão."""
res = int(valor)
print(res)
print(type(res))

#Podemos trabalhar com números complexos