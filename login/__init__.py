from time import sleep
from cadastrar import lista_user, lista_senha, linha



def login():
    while True:
        print('\033[036mFaça seu login\033[m'.center(80))
        linha()
        print('\033[036mDigite \033[033m[SAIR] \033[036mno login para retornar\033[m'.center(86))
        linha()
        nome = str(input('\033[033mLogin: \033[m')).lower()
        if nome == 'sair':
            print('\033[036mRetornando ao menu anterior\033[m'.center(80))
            sleep(1)
            linha()
            break
        if nome in lista_user:
            ind = nome.index(nome)
            senha = str(input('\033[033mSenha: \033[m'))
            if lista_senha[ind] == senha:
                print('\033[036mAcessoando banco de dados...'.center(80))
                sleep(1)
                print('Login realizado com sucesso\033[m'.center(80))
                break
            else:
                linha()
                print('\033[036mAcessoando banco de dados...\033[m'.center(80))
                sleep(1)
                linha()
                print('\033[031mERRO! Senha não confere\033[m'.center(80))
                linha()
        else:
            if nome not in lista_user:
                sleep(1)
                linha()
                sleep(1)
                print('\033[031mERRO! Usuário não está cadastrado\033[m'.center(76))
                linha()
