# Módulos
import V2.podserv as podserv
import V2.usuarios as usuarios

dados_usuario = [['dom', 'd@.com', '123456789', 1], ['jonas', 'j@.com', '28032004', 2]]

# Produtos e serviços
produto = [['COLEIRA', 'CACHORRO', 25, 20]]
servico = [['banho',50],['tosa completa', 70],['tosa bb',50]]
profissionais = []
pets = [['spyke']]
carrinho = [['coleira']]
agenda = [['banho']]
pets_venda = [['ZEUS', 'cachorro', 10, 'masculino']]
# Sistema funcionando
print("BEM-VINDO AO PET SERTÃO\nLUGAR DE MUITO AMOR E COMPAIXÃO")

while True:
    menu = int(input('Deseja fazer login ou cadastro?\n1 - Cadastro\t2 - Login\t3 - Sair\n'))
    if menu == 1:
        usuarios.cadastrar_usuario(dados_usuario)

        print(f'Cadastro feito com sucesso!')
        continue

    elif menu == 2:
        print('OPÇÃO ESCOLHIDA: LOGIN')

        usuarios.login_usuario(dados_usuario)
            # break
"""
        for tipo in dados_usuario:
            # Menu ADM
            if tipo[3] == 1 and tipo[1] == emailusuario:
                while True:
                    print('SISTEMA DE GERENCIAMENTO DE PRODUTOS E SERVIÇOS\n\tPETSERTÃO')
                    opcao_usuario = int(input("Opções:\n"
                                                "1 - Cadastrar produtos/serviços ou pet\n"
                                                "2 - Buscar produto/serviço ou pet\n"
                                                "3 - Cadastrar profissionais\n"
                                                "4 - Atualizar dados de profissional\n"
                                                "5 - Atualizar dados de produto e serviço ou pet\n"
                                                "6 - Remover dados\n"
                                                "7 - Imprimir dados\n"
                                                "8 - Sair\n"))

                    if opcao_usuario == 1:
                        tipo_acao = int(input("1 - Produto 2 - Serviço 3 - Pet"))
                        if tipo_acao == 1:
                            podserv.cadastrar_produto(produto)

                        elif tipo_acao == 2:
                            nomeservico = input('Digite o nome do serviço: ').upper()
                            categoria_pet = input('Digite o categoria de animal do produto: ').upper()
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
                                                    dados_servico = [nomeservico, categoria_pet, hora_func]
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

                        elif tipo_acao == 3:
                            identificador = int(input('Identificador do pet: '))
                            raca_pet = input('Raça do pet: ').upper()
                            valor_pet = float(input('Preço: '))
                            qtnd_disponivel = int(input('Quantidade disponível: '))
                            dados_pet = [identificador, raca_pet, valor_pet, qtnd_disponivel]
                            pets_venda.append(dados_pet)
                            continue

                    elif opcao_usuario == 2:
                        nomeprodserv = input('Digite o nome do produto, serviço ou pet: ').upper()
                        tipo = int(input('1 - Produto\t2 - Serviço:\n3 - Pets'))
                        if tipo == 1:
                            for produtinhos in produto:
                                if nomeprodserv == produtinhos[0]:
                                    print(f'Dados do produto: {produtinhos[produtinhos.index(nomeprodserv)]}')
                                else:
                                    print('NÃO ENCONTRADO')

                        elif tipo == 2:
                            for servicinhos in servico:
                                if nomeprodserv == servicinhos[0]:
                                    print(f'Dados do Serviço: {servicinhos[servicinhos.index(nomeprodserv)]}')
                                else:
                                    print('NÃO ENCONTRADO')

                        elif tipo == 3:
                            for petsinhos in pets_venda:
                                if petsinhos[0] == nomeprodserv:
                                    print(f'Dados do pet: {petsinhos[petsinhos.index(nomeprodserv)]}')
                                else:
                                    print('NÃO ENCONTRADO')

                    elif opcao_usuario == 3:
                        nomeprof = input('Nome do profissional: ').upper()
                        opcupacao = input('Ocupação: ').upper()
                        while True:
                            hora_prof_init = int(input('Digite a hora de chegada: '))
                            hora_prof_final = int(input('Digite a hora de saída: '))
                            if (hora_prof_init > 6 and hora_prof_init < 16) and (
                                    hora_prof_final > 8 and hora_prof_final < 18):
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
                                    produtinhos[1] = input('Digite a categoria: ').upper()
                                    produtinhos[2] = float(input('Digite o valor do produto: '))
                                    produtinhos[3] = int(input('Digite a quantidade disponível: '))

                                    print('Atualização feita com sucesso!')
                        elif tipo == 2:
                            for servicinhos in servico:
                                if nomeprodserv == servicinhos[0]:
                                    servicinhos[0] = input('Digite o nome do serviço: ').upper()
                                    servicinhos[1] = input('Digite a categoria: ').upper()
                                    servicinhos[2] = float(input('Digite o valor do serviço: '))
                                    servicinhos[3] = int(input('Digite o horário de funcionamento: '))

                                    print('Atualização feita com sucesso!')

                        elif tipo == 3:
                            for petsinhos in pets_venda:
                                if petsinhos[1] == nomeprodserv:
                                    petsinhos[0] = input('Digite a espécie do pet: ').upper()
                                    petsinhos[1] = int(input('Digite a categoria: ').upper())
                                    petsinhos[2] = float(input('Digite o valor do pet: '))
                                    petsinhos[3] = int(input('Digite a quantidade disponível: '))

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
                                if tipo_do_user[3] == 1:
                                    print(f'Nome do ADM: {tipo_do_user[0]}\nE-mail: {tipo_do_user[1]}')
                        elif tipo_do_user == 2:
                            for tipo_do_user in dados_usuario:
                                if tipo_do_user[3] == 2:
                                    print(f'Nome do cliente: {tipo_do_user[0]}\nE-mail: {tipo_do_user[1]}')

                    elif opcao_usuario == 8:
                        break

            # Menu clientes
            elif tipo[3] == 2 and tipo[1] == emailusuario:
                while True:
                    print('1 - Cadastrar meu pet (só vale 1)')
                    print('2 - Comprar produto')
                    print('3 - Agendar serviço')
                    print('4 - Comprar pet')
                    print('5 - Meu carrinho')
                    print('6 - Sair')

                    opcao = int(input('Escolha uma opção: '))

                    # Cadastrar cliente
                    if opcao == 1:
                        nome_pet = input('Nome do pet: ').lower()
                        tipo_pet = input('Tipo do pet: cachorro, gato, etc: ').lower()

                        cadastro_pet = [nome_pet, tipo_pet]
                        pets.append(cadastro_pet)
                        print('\n Cadastro realizado com sucesso!')
                        print(f'Nome do pet: {nome_pet}\nTipo: {tipo_pet}\n')

                    # comprar produto
                    elif opcao == 2:
                        while True:
                            produtos_cad = len(produto)

                            if produtos_cad == 0:
                                print('LISTA DE PRODUTOS VAZIA\nAGUARDE PARA MAIS NOVIDADES!')
                                break
                            else:
                                for m in produto:
                                    print(f'Produto: {m[0]}\nCategoria: {m[1]}\nPreço: R${m[2]}\nQuantidade disponível: {m[3]}')
                                    
                                    while True:
                                        categoria_cliente = input('Digite a categoria do produto: ').upper()
                                        for c in produto:
                                            if categoria_cliente == c[1]:
                                                print(c)
                                            else:
                                                print('CATEGORIA INEXISTENTE')
                                                
                                        deseja_sair = int(input('Deseja sair?\n1 - Sim\t2 - Não'))
                                        if deseja_sair == 1:
                                            break
                                        elif deseja_sair == 2:
                                            continue
                                        else:
                                            print('OPÇÃO INVÁLIDA')

                            escolha = input("\nDigite o nome do produto que deseja comprar\nDIGITE 'SAIR' PARA SAIR\n").upper()

                            if escolha == 'SAIR':
                                break

                            else:
                                for n in produto:
                                    if n[0] == escolha:
                                        minhas_compras = [n]
                                        carrinho.append(minhas_compras)
                                        print('ADICIONADO AO CARRINHO!')

                    # agendar serviço
                    elif opcao == 3:
                        while True:
                            serv_desejado = input('Nome do serviço desejado: ').upper()

                            if len(servico) == 0:
                                print('LISTA DE SERVIÇOS VAZIA\nAGUARDE PARA MAIS NOVIDADES!')
                                break
                            else:
                                for m in servico:
                                    print(f'Serviço: {m[0]}\nPreço: R${m[1]}\nHorário disponível: {m[2]}')

                            escolha = input(
                                "\nDigite o nome do serviço que deseja contratar\nDIGITE 'SAIR' PARA SAIR\n").upper()
                            hora_escolha = int(input('Digite a hora que deseja realizar o serviço: '))

                            if escolha == 'SAIR':
                                break

                            else:
                                for n in servico:
                                    if n[3] <= hora_escolha:
                                        if n[0] == escolha:
                                            carrinho.append(n[0])
                                    else:
                                        print('HORÁRIO INDISPONÍVEL')
                    
                    # comprar pet
                    elif opcao == 4:
                        while True:
                            pets_disponiveis = input('Espécie que você procura: ').upper()
                            if len(pets_venda) == 0:
                                print('Nenhum pet disponivel\nAguarde Novidades!')
                                break
                            else:
                                for p in pets_venda:
                                    if p[1] == pets_disponiveis and p[3] != 0:
                                        print(
                                            f'Identificador: {p[0]}\nEspécie: {p[1]}\n Preço: {p[2]}\nQuantidade: {p[3]}')

                                codigo_pet_compra = int(input('Insira o código do pet que você deseja comprar: '))
                                for code in pets_venda:
                                    if code[0] == codigo_pet_compra:
                                        carrinho.append(code[1])
                                        print('Compra realizada com sucesso!')

                    # sair
                    elif opcao == 6:
                        print('OBRIGADO POR USAR O NOSSO SISTEMA!')
                        break
                    # Opção inválida
                    else:
                        print('OPÇÃO INVÁLIDA\nTENTE NOVAMENTE')

elif menu == 3:
    print('OBRIGADO POR USAR O PETSERTÃO!')
    break
    
    """