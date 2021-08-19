# 1
num1 = input('1-Digite um numero:')
num2 = input('1-Digite outro numero:')

if num1 > num2:
    print('1º numero é maior\n')
else:
    print('2º numero é maior\n')

# 2
num = float(input('2-Digite um numero positivo:'))

if num > 0:
    R = float(num) ** 0.5
    print(f'A raiz quadrada de {num} é {R}\n')
else:
    print('numero invalido\n')

# 3
num = float(input('3-Digite um numero:'))

if num > 0:
    R = float(num) ** 0.5
    print(f'A raiz quadrada de {num} é {R}\n')
else:
    R = float(num) ** 2
    print(f'{num} ao quadrado é {R}\n')

# 4
num = float(input('4-Digite um numero positivo:\n'))

if num > 0:
    Q = num ** 2
    R = num ** 0.5
    print(f'{num} ao quadrado é {Q} e sua raiz quadrada {R}.\n')

# 5
num = int(input('5-Digite um numero inteiro:'))
X = num % 2

if X == 0:
    print('PAR\n')
else:
    print('IMPAR\n')

# 6
num = int(input('6-Digite um numero inteiro:'))
num1= int(input('6-Digite outro numero inteiro:'))

if num > num1:
    print(f'O primeiro numero é o maior, e a diferença entre eles é {num - num1}\n')
else:
    print(f'O segundo numero é o maior, e a diferença entre eles é {num1 - num}\n')

# 7
num = int(input('7-Digite um numero inteiro:'))
num1 = int(input('7-Digite outro numero inteiro:'))

if num > num1:
    print('O primeiro numero é o maior\n')
elif num == num1:
    print('Números iguais\n')
else:
    print('O segundo número é o maior\n')

# 8
num = float(input('8-Digite sua primeira nota:'))
num1 = float(input('8-Digite sua segunda nota:'))

if num >= 0 and num <= 10 and num1 >= 0 and num1 <= 10 :
    R = (num + num1) / 2
    print(f'Sua média é {R}\n')
else:
    print('Numero invalido\n')

# 9
S = float(input('Digite seu salário:'))
P = float(input('Digite o valor das parcelas que você que você deseja pagar:'))
M = (20/100)*S

if P >= M:
    print('Emprestimo concedido\n')
else:
    print('Emprestimo não concedido\n')

# 10
print('10-Calculo do peso ideal')
S = input('10-Responda qual o seu sexo, H para Homem e M para mulher:')
h = float(input('10-Agora diga sua altura:'))

if S == 'H':
    r = (72.7 * h) - 58
    print(f'Seu peso ideal é {r}Kg\n')
elif S == 'M':
    r2 = (62.1 * h) - 44.7
    print(f'Seu peso ideal é {r2}Kg\n')
















