# Menu principal

# Dados do usuário
dados_nome = []
dados_email = []
dados_senha = []
dados_tipo = []

# Produtos e serviços
prod_serv = []

# Sistema funcionando
print("Bem-vindo ao PetSertão\nLugar de muito amor e compaixão")

while True:
    menu = int(input('Deseja fazer login ou cadastro?\n1 - Cadastro\t2 - Login\t3 - Sair\n'))
    if menu == 1:
        print('OPÇÃO ESCOLHIDA: CADASTRO')

        nomeusuario = input('Digite o seu nome de usuário: ').lower()
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

        dados_nome.append(nomeusuario)
        dados_email.append(emailusuario)
        dados_senha.append(senhausuario)
        dados_tipo.append(tipousuario)

        print('Login bem-sucedido!')
        print(f'Bem-vindo(a), {nomeusuario}!')

    elif menu == 2:
        print('OPÇÃO ESCOLHIDA: LOGIN')

        nomeusuario = input('Digite o seu nome de usuário: ').lower()
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

        for i in dados_nome:
            if i == nomeusuario:
                for j in dados_email:
                    if j == emailusuario:
                        for k in dados_senha:
                            if k == senhausuario:
                                print('Login bem-sucedido!')
                                print(f'Dados do usuário:\n'
                                      f'Nome: {nomeusuario}\tPosição: {dados_nome.index(i)}\n'
                                      f'E-mail: {emailusuario}\tPosição: {dados_email.index(j)}\n')

    else:
        print('Obrigado por usar nosso sistema\nO PetSertão agradece! Volte sempre!')
        break

# Sistema do ADM
while True:
    if tipousuario == 1:
        print('SISTEMA DE GERENCIAMENTO DE PRODUTOS E SERVIÇOS\n\tPETSERTÃO')
        opcao_usuario = int(input("Opções:\n"
                                  "1 - Cadastrar produtos/serviços\n"
                                  "2 - Buscar produto/serviço\n"
                                  "3 - Atualizar dados\n"
                                  "4 - Remover dados\n"))
        if opcao_usuario == 1:
            dados_prodserv = []
            tipo = int(input('1 - Produto\t2 - Serviço\n'))
            dados_prodserv.append(tipo)
            nome_prodserv = input('Produto/serviço: ')
            dados_prodserv.append(nome_prodserv)
            if tipo == 2:
                horarios = input("Horário (08h:18h): ")
                dados_prodserv.append(horarios)
            valor = float(input('Valor do produto/serviço: '))
            dados_prodserv.append(valor)
            prod_serv.append(dados_prodserv)
        elif opcao_usuario == 2:
            nome_prodserv = input('Produto/serviço: ')
            for i in dados_prodserv:
                if nome_prodserv in prod_serv[dados_prodserv[1]]:
                    print(f'Produto/Serviço: {nome_prodserv}'
                          f'Tipo: {prod_serv[dados_prodserv[0]]}'
                          f'Valor: {prod_serv[dados_prodserv[-1]]}')
        elif opcao_usuario == 3:
            nome_prodserv = input('Produto/serviço: ')
            for i in dados_prodserv:
                if nome_prodserv in prod_serv[dados_prodserv[1]]:
                    print('NÃO É POSSÍVEL ALTERAR O TIPO')
                    dados_prodserv[0] = input('Produto/serviço: ')