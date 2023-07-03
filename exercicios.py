
# print(12, 23, sep='meu pau', end='kkk')

# pratica de f string
# nome = input('digite seu nome: ')
# idade = input('digite sua idade: ')

# if nome and idade:
#     print(f'seu nome é: {nome}')
#     print(f'você tem: {idade} anos')
#     print(f'seu nome invertido é: {nome[::-1]}')
#     if ' ' in nome:
#         print('seu nome tem espaços')
#     else:
#         print('seu nome não tem espaços')
#     print(f'seu nome tem {len(nome)} letras')
#     print(f'a primeira letra do seu nome é {nome[0]}')
#     print(f'a ultima letra do seu nome é {nome[-1]}')

# else:
#     print('desculpe, mas voccê não digitou nada')


# try e exception 

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são ivalidos')
        continue

    operadores_permitidos ='+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue
    if len(operador) >1:
        print('Escolha somente um operador')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '-':
        print(f'{numero_1}-{numero_2} =', numero_1 - numero_2)
    elif operador == '+':
        print(f'{numero_1}+{numero_2} =', numero_1 + numero_2)
    elif operador == '/':
        print(f'{numero_1}/{numero_2} =', numero_1 / numero_2)
    elif operador =='*':
        print(f'{numero_1}*{numero_2} =', numero_1 * numero_2)
    else:
        print('Você nunca deveria ter vhegado aqui')

    sair = input('Quer sair? digite [s]im: ').lower().startswith('s')

    if sair is True:
        break


# def saudacao(nome):
#     print(f'Olá {nome}! seja muito bem vindo')


# saudacao(input('insira seu nome: '))