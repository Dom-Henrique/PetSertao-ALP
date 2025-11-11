def cadastrar_usuario(dados_usuario):
    while True:
        nomeusuario = input('Digite o seu nome de usuário: ').lower()
        if len(nomeusuario) >= 3:
            break
        else:
            print('NOME DE USUÁRIO MUITO CURTO')
    while True:
        emailusuario = input('Digite um e-mail válido: ').lower()
        if '@' in emailusuario and '.com' in emailusuario:
            break
        else:
            print('E-MAIL INVÁLIDO')

    while True:
        senhausuario = input('Digite uma senha de no mínimo 8 dítigos: ')
        if len(senhausuario) < 8:
            print('SENHA MUITO CURTA')
        else:
            break

    tipousuario = int(input('Qual o seu tipo de usuário?\n1 - Administrador\t2 - Cliente\n'))

    dados_cadastro = [nomeusuario, emailusuario, senhausuario, tipousuario]
    dados_usuario.append(dados_cadastro)

    print(f'Cadastro feito com sucesso!')
    
def login_usuario(dados_usuario):
    while True:
            emailusuario = input('Digite um e-mail válido: ').lower()
            if '@' in emailusuario and '.com' in emailusuario:
                break
            else:
                print('E-MAIL INVÁLIDO')

    while True:
        senhausuario = input('Digite uma senha de no mínimo 8 dítigos: ')
        if len(senhausuario) < 8:
            print('SENHA MUITO CURTA')
        else:
            break

    # Laço de repetição percorre a lista e encontra os dados de acordo com o usuario

    for i in dados_usuario:
        if i[1] == emailusuario and i[2] == senhausuario:
            print(f'Usuário encontrado com sucesso!\nNome: {i[0]}\nE-mail: {i[1]}\n')
            if i[3] == 1:
                print(f'Tipo: ADM')
            elif i[3] == 2:
                print(f'Tipo: CLIENTE')