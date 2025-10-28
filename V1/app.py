dados_usuario = []

# Produtos e serviços
produto = []
servico = []
profissionais = []
pets = []

# Sistema funcionando
print("Bem-vindo ao Pet Sertão\nLugar de muito amor e compaixão")

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

        dados_cadastro = [nomeusuario, emailusuario, senhausuario, tipousuario]
        dados_usuario.append(dados_cadastro)

        print(f'Cadastro feito com sucesso!')
        continue

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

        for i in dados_usuario:
            if i[0] == nomeusuario and i[1] == emailusuario and i[2] == senhausuario:
                print(f'Usuário encontrado com sucesso!\nNome: {i[0]}\nE-mail: {i[1]}\n')
                if i[3] == 1:
                    print(f'Tipo: ADM')
                elif i[3] == 2:
                    print(f'Tipo: CLIENTE')
            break

        else:
            print('TENTE NOVAMENTE')
            continue

        break
    elif menu == 3:
        print('Obrigado por usar nosso sistema\nO PetSertão agradece! Volte sempre!')
        break
    else:
        print('INVÁLIDO')

# Sistemas
while True:
    for tipo in dados_usuario:
        # Menu ADM
        if tipo[3] == 1 and tipo[0] == nomeusuario:
            print('SISTEMA DE GERENCIAMENTO DE PRODUTOS E SERVIÇOS\n\tPETSERTÃO')
            opcao_usuario = int(input("Opções:\n"
                                      "1 - Cadastrar produtos/serviços\n"
                                      "2 - Buscar produto/serviço\n"
                                      "3 - Cadastrar profissionais\n"
                                      "4 - Atualizar dados de profissional"
                                      "5 - Atualizar dados de produto e serviço\n"
                                      "6 - Remover dados\n"
                                      "7 - Imprimir dados\n"
                                      "8 - Sair\n"))

            if opcao_usuario == 1:
                tipo_acao = int(input("1 - Produto\t2 - Serviço\n"))
                if tipo_acao == 1:
                    nomeproduto = input('Digite o nome do produto: ').upper()
                    produtovalor = float(input('Digite o valor do produto: '))
                    qtnd_disponivel = int(input('Digite a quantidade no estoque: '))

                    dados_produto = [nomeproduto, produtovalor, qtnd_disponivel]

                    produto.append(dados_produto)
                    print('Cadastro bem-sucedido!')

                elif tipo_acao == 2:
                    nomeservico = input('Digite o nome do serviço: ').upper()
                    descservico = input('Dê uma descrição do serviço: ')
                    while True:
                        profissional = input('Nome do profissional: ').upper()
                        controle1 = False
                        for profissionalzinha in profissionais:
                            if profissionalzinha[0] == profissional:
                                print('PROFISSIONAL ENCONTRADO(A)')
                                controle1 = True
                                servicovalor = float(input('Valor do serviço: '))
                                while True:
                                    hora_func = int(input('Hora do serviço: '))
                                    controle2 = False

                                    for horario in profissionais:
                                        if horario[2] <= hora_func and horario[3] > hora_func:
                                            dados_servico = [nomeservico, servicovalor, hora_func]
                                            servico.append(dados_servico)
                                            print('SERVIÇO CADASTRADO COM SUCESSO!')
                                            controle2 = True
                                    if controle2:
                                        break
                                    else:
                                        print('HORÁRIO INCORRETO')
                                        continue
                        if controle1 == False:
                            print('PROFISSIONAL NÃO ENCONTRADO(A)')
                            break

            elif opcao_usuario == 2:
                nomeprodserv = input('Digite o nome do produto: ').upper()
                tipo = int(input('1 - Produto\t2 - Serviço:\n'))
                if tipo == 1:
                    for produtinhos in produto:
                        if nomeprodserv == produtinhos[0]:
                            print(f'Dados do produto: {produtinhos[produtinhos.index(nomeprodserv)]}')
                elif tipo == 2:
                    for servicinhos in servico:
                        if nomeprodserv == servicinhos[0]:
                            print(f'Dados do Serviço: {servicinhos[servicinhos.index(nomeprodserv)]}')

            elif opcao_usuario == 3:
                nomeprof = input('Nome do profissional: ').upper()
                opcupacao = input('Ocupação: ').upper()
                while True:
                    hora_prof_init = int(input('Digite a hora de chegada: '))
                    hora_prof_final = int(input('Digite a hora de saída: '))
                    if (hora_prof_init > 6 and hora_prof_init < 16) and (hora_prof_final > 8 and hora_prof_final < 18):
                        break
                    else:
                        print("FUNCIONAMENTO APENAS DE 6H ÀS 18H\nTENTE NOVAMENTE")

                prof_clinica = [nomeprof, opcupacao, hora_prof_init, hora_prof_final]
                profissionais.append(prof_clinica)

            elif opcao_usuario == 4:
                profissional = input('Nome do(a) profissional: ').upper()
                for i in profissionais:
                    if i[0] == profissional:
                        i[0] = input('Nome do profissional: ').upper()
                        i[1] = input('Ocupação: ').upper()
                        while True:
                            i[2] = int(input('Digite a hora de chegada: '))
                            i[3] = int(input('Digite a hora de saída: '))
                            if (i[2] > 6 and i[2] < 16) and (i[3] > 8 and i[3] < 18):
                                break
                            else:
                                print("FUNCIONAMENTO APENAS DE 6H ÀS 18H\nTENTE NOVAMENTE")

            elif opcao_usuario == 5:
                nomeprodserv = input('Digite o nome do produto: ').upper()
                tipo = int(input('1 - Produto\t2 - Serviço:\n'))
                if tipo == 1:
                    for produtinhos in produto:
                        if nomeprodserv == produtinhos[0]:
                            produtinhos[0] = input('Digite o nome do produto: ').upper()
                            produtinhos[1] = input('Digite o valor do produto: ')
                            produtinhos[2] = input('Digite a quantidade disponível: ')

                            print('Atualização feita com sucesso!')
                elif tipo == 2:
                    for servicinhos in servico:
                        if nomeprodserv == servicinhos[0]:
                            servicinhos[0] = input('Digite o nome do serviço: ').upper()
                            servicinhos[1] = input('Digite o valor do serviço: ')
                            servicinhos[2] = input('Digite o horário de funcionamento: ')

                            print('Atualização feita com sucesso!')

            elif opcao_usuario == 6:
                nomeprodserv = input('Digite o nome do produto/serviço: ').upper()
                tipo = int(input('1 - Produto\t2 - Serviço:\n'))
                if tipo == 1:
                    for produtinhos in produto:
                        if nomeprodserv == produtinhos[0]:
                            produto.clear()

                            print('Atualização feita com sucesso!')
                elif tipo == 2:
                    for servicinhos in servico:
                        if nomeprodserv == servicinhos[0]:
                            servico.clear()

                            print('Atualização feita com sucesso!')

            elif opcao_usuario == 7:
                tipo_do_user = int(input('1 - ADM\t2 - Cliente'))
                if tipo_do_user == 1:
                    for tipo_do_user in dados_usuario:
                        if tipo_do_user[4] == 1:
                            print(f'Nome do ADM: {tipo_do_user[0]}\nE-mail: {tipo_do_user[1]}')
                elif tipo_do_user == 2:
                    for tipo_do_user in dados_usuario:
                        if tipo_do_user[4] == 2:
                            print(f'Nome do cliente: {tipo_do_user[0]}\nE-mail: {tipo_do_user[1]}')

            elif opcao_usuario == 8:
                break
        # Menu clientes
        elif tipo[3] == 2 and tipo[0] == nomeusuario:
            while True:
                print('1 - Cadastrar meu pet (só vale 1)')
                print('2 - Meu pet')
                print('5 - Sair')

                opcao = input('Escolha uma opção: ')

                # Cadastrar cliente
                if opcao == '1':
                    nome_pet = input('Nome do pet: ').lower()
                    tipo_pet = input('Tipo do pet: cachorro, gato, etc: ').lower()
                    servico = input('Serviço desejado: banho, tosa, vacina, etc: ').lower()

                    cadastro_pet = [nome_pet, tipo_pet, servico]
                    pets.append(cadastro_pet)
                    print('\n Cadastro realizado com sucesso!')

                # Listar pets
                elif opcao == '2':
                    indice_usuario = tipo.index(nomeusuario)
                    print(f'Pet do cliente {nomeusuario}: {pets[indice_usuario]}\n')

                # Remover cliente
                elif opcao == '4':
                    pass
                # Sair do sistema
                elif opcao == '5':
                    print('\n Volte sempre ao Pet Sertão!')
                    break

                # Opção inválida
                else:
                    print('\n Opção inválida! Tente novamente.')