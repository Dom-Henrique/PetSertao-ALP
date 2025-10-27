dados_usuario = []

# Produtos e serviços
produto = []
servico = []
clientes = []
pets = []

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
                print(f'Usuário encontrado com sucesso!\nNome: {i[0]}\nE-mail: {i[1]}\nTipo: {i[3]}')

            else:
                print('TENTE NOVAMENTE')

        break
    else:
        print('Obrigado por usar nosso sistema\nO PetSertão agradece! Volte sempre!')
        break

# Sistema do ADM
while True:
    for tipo in dados_usuario:
        if tipo[3] == 1 and tipo[0] == nomeusuario:
            print('SISTEMA DE GERENCIAMENTO DE PRODUTOS E SERVIÇOS\n\tPETSERTÃO')
            opcao_usuario = int(input("Opções:\n"
                                      "1 - Cadastrar produtos/serviços\n"
                                      "2 - Buscar produto/serviço\n"
                                      "3 - Atualizar dados\n"
                                      "4 - Remover dados\n"
                                      "5 - Sair\n"))

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
                    servicovalor = float(input('Digite o valor do produto: '))
                    horario_func = input('Digite o horário de funcionamento: ')

                    dados_servico = [nomeservico, servicovalor, horario_func]

                    servico.append(dados_servico)
                    print('Cadastro bem-sucedido!')

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

            elif opcao_usuario == 4:
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

            elif opcao_usuario == 5:
                break
        # Menu clientes
        elif tipo[3] == 2 and tipo[0] == nomeusuario:
            while True:
                print('1 - Cadastrar pets')
                print('2 - Listar pets')
                print('3 - Buscar pet por nome')
                print('5 - Sair')

                opcao = input('Escolha uma opção: ')

                # Cadastrar cliente
                if opcao == '1':
                    nome_cliente = input('Nome do cliente: ')
                    nome_pet = input('Nome do pet: ')
                    tipo_pet = input('Tipo do pet: cachorro, gato, etc: ')
                    servico = input('Serviço desejado: banho, tosa, vacina, etc: ')

                    cadastro = [nome_cliente, nome_pet, tipo_pet, servico]
                    clientes.append(cadastro)
                    print('\n Cadastro realizado com sucesso!')

                # Listar todos os clientes e pets
                elif opcao == '2':
                    if len(clientes) == 0:
                        print('\n Nenhum cliente cadastrado ainda.')
                    else:
                        print('\n Lista de clientes e pets:')
                        for c in clientes:
                            print(f'Cliente: {c[0]} | Pet: {c[1]} ({c[2]}) | Serviço: {c[3]}')

                # Buscar pet por nome
                elif opcao == '3':
                    nome_busca = input('Digite o nome do pet: ')
                    encontrado = False

                    for c in clientes:
                        if c[1].lower() == nome_busca.lower():
                            print('\n Pet encontrado!')
                            print(f'Dono: {c[0]} | Tipo: {c[2]} | Serviço: {c[3]}')
                            encontrado = True
                            break

                    if not encontrado:
                        print('\n Pet não encontrado.')

                # Remover cliente
                elif opcao == '4':
                    nome_remover = input('Digite o nome do cliente a remover: ')
                    removido = False

                    for c in clientes:
                        if c[0].lower() == nome_remover.lower():
                            clientes.remove(c)
                            print('\n Cliente removido com sucesso!')
                            removido = True
                            break

                    if not removido:
                        print('\n Cliente não encontrado.')

                # Sair do sistema
                elif opcao == '5':
                    print('\n Obrigado por usar o Petshop!')
                    break

                # Opção inválida
                else:
                    print('\n Opção inválida! Tente novamente.')
