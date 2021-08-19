
"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é ddi tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples: ex: 'Marcos'
- Aspas duplas: ex: "Marcos"
- Aspas simples triplas: ex: '''Marcos'''
"""
# - Aspas duplas triplas: ex: """Marcos"""

#  Entrada de dados
print("Qual é o seu nome?")
nome = input()  #ENTRADA

#  Processamento

# Saída de dados
# Exemplo de print 'antigo'
print("Seja bem-vindo(a) %s" % nome)
print("Qual a sua idade?")
idade = input()

print("O %s têm %s anos de idade." % (nome, idade))

# Exemplo de print 'moderno' criado 3.x versão
print('Qual seu nome?')
nome = input()

print('Seja bem-vindo(a) {0}'.format(nome))

print('Qual sua idade?')
idade = input()

print('O {0} têm {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' criado 3.7 versão
nome = input('Qual o seu nome?')

print(f'Seja bem-vindo(a) {nome}')
idade = input('Qual a sua idade?')

print(f'O {nome} têm {idade} anos de idade.')

"""
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'O {nome} nasceu em {2021 - int(idade)}')

