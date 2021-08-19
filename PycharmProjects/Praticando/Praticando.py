dir ('GEEK')


print("Olá, somos da M&R negócios e iremos lhe fazer algumas perguntas para realizar o seu cadastro")

#ENTRADA DE DADOS
nome = input('Informe seu nome completo?')
nome = nome.title()
ano = int(input('Informe em que ano você nasceu?'))
cpf = input('Informe os digitos do seu CPF?')
rg = input('Informe os digitos do seu RG?')
endereço = input('Aonde você mora?')

#RETORNO DO SISTEMA
print(f'NOME: {nome}'
      f'\nANO DE NASCIMENTO: {ano}'
      f'\nSUA IDADE é:  {2021 - ano}'
      f'\nO seu CPF é: {cpf}'
      f'\nO seu RG é: {rg}'
      f'\nVocê mora no endereço: {endereço}')