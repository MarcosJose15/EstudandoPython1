"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
"""

# and
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# or
ativo = False
logado = True

if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# not
# Se não estiver ativo

ativo = False
logado = True

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

# is
# comparação

ativo = False
logado = True

if ativo is False:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')