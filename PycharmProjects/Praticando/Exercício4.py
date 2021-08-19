"""
ATIVIDADE DO MÓDULO 4
"""


# 1
numero = int(input('1-Digite um número inteiro:'))
print(numero)
print(type(numero))
print('\n')

# 2
numero = float(input('2-Digite um número real:'))
print(numero)
print(type(numero))
print('\n')

# 3
num1 = int(input('3-Digite um valor:'))
num2 = int(input('3-Digite um segundo valor:'))
num3 = int(input('3-Digite um terceiro valor:'))
print('\n')
print(num1+num2+num3)
print('\n')

# 4
num = int(input('4-Digite um numero real:\n'))
print(num**2)
print('\n')

# 5
num = float(input('5-Digite um número real:\n'))
print(num/5)
print('\n')

# 6
C = float(input("""6-Agora vamos converter a temperetura de grau Celcius para Fahrenheit, 
Digite a tempetura em graus Celcius:\n """))
F = C *(9.0/5.0) + 32.0
print(f'A temperatura em Fahrenheit é {F} F\n' )

# 7
F = float(input("""7-Agora vamos converter a tempetura de Fahrenheit para graus Celcius, 
agora digite a tempetura em Fahrenheit:\n """))
C = 5.0*(F-32.0)/9.0
print(f'A tempetura em Celcius é {C}ºC\n')

# 8
K = float(input("""8-Agora vamos converter a temperatura de Kelvin para graus Celsius. 
Digite a temperatura em Kelvin:\n """))
C = K-273.15
print(f'A tempetura em Celcius é {C}ºC\n')

# 9
C = float(input("""9-Agora vamos converter a temperatura de graus Celsius  para Kelvin. 
Digite a temperatura em graus Celsius:\n """))
K = C + 273.15
print(f'A tempetura em Kelvin é {K} \n')

# 10
K = float(input("""10-Iremos converter a velocidade de Km/h para m/s, 
Digite a velocidade em Km/h:\n"""))
M = K/3.6
print(F'A velocidade em m/s é {M}m/s\n')

# 11
M = float(input("""11-Iremos converter a velocidade de m/s para km/h, 
Digite a velocidade em m/s:\n"""))
K = M * 3.6
print(F'A velocidade em km/h é {K}km/h\n')

# 12
M = float(input('De milhas para quilometros\n:'))
K = 1.61*M
print(K)
print('\n')

# 13
K = float(input('De quilometros para milha:\n'))
M = K/1.61
print(M)
print('\n')

# 14
G = float(input('''ângulo em graus convertido em radianos''')
R = G*3.14/180
print(R)
print('''\n''')

# 15





























