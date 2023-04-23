from time import sleep

def linha(tam=30):
    print('=-' * tam)


lista_user = ['larissa', 'thiele', 'alvaro']
lista_senha = ['Gamora', 'Thor', 'Arvo88']


def novo():
    while True:
        linha()
        print('\033[036mCadastro de novo usuário\033[m'.center(80))
        print('\033[036mDigite \033[033m[SAIR] \033[036mno login para retornar\033[m'.center(86))

        linha()
        nome = str(input('\033[036mDigite seu nome de usuário: \033[m')).lower()

        if nome == 'sair':
            print('\033[036mRetornando ao menu anterior\033[m'.center(80))
            sleep(1)
            linha()
            break

        linha()
        if nome in lista_user:
            sleep(1)
            print('\033[031mERRO! Nome de usuário já cadastrado: \033[m')
        else:
            senha = str(input('\033[035mDigite sua senha: \033[m'))
            sleep(1)
            senha2 = str(input('\033[035mRepita sua senha: \033[m'))
            if senha == senha2:
                lista_user.append(nome)
                lista_senha.append(senha)
                linha()
                sleep(1)
                print('\033[032mCadastro realizado com sucesso\033[m'.center(80))
                break
            else:
                sleep(1)
                print('\033[031mERRO! Você digitou senhas diferentes\033[m')
