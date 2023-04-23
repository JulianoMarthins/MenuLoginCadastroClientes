from time import sleep
import cadastrar
import login

cadastrar.linha()
print('\033[035mProgramado por JulianoMarthins\033[m'.center(80))
cadastrar.linha()



while True:
    print('\033[033m1\033[m - \033[036mFazer login\033[m\n'
          '\033[033m2\033[m - \033[036mCadastrar usuário\033[m\n'
          '\033[033m3\033[m - \033[036mFechar programa\033[m')

    cadastrar.linha()

    while True:
        cond = str(input('\033[035mDigite sua opção: \033[m'))
        try:
            cond = int(cond)
            if cond >= 1 and cond <= 3:
                break
            else:
                print('\033[031mERRO! Você digitou um valor inválido\033[m')
                sleep(1)
        except:
            print('\033[031mERRO! Você digitou um valor inválido\033[m')
            sleep(1)

    match cond:
        case 1:
            cadastrar.linha()
            print('\033[033mAcessando\033[m'.center(80))
            sleep(1)
            login.login()
            sleep(1)
        case 2:
            cadastrar.linha()
            print('\033[033mAcessando\033[m'.center(80))
            sleep(1)
            cadastrar.novo()
            sleep(1)
        case 3:
            cadastrar.linha()
            print('\033[036mFechando programa'.center(80))
            sleep(1)
            print('Obrigado\033[m'.center(80))
            cadastrar.linha()
            break
