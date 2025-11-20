from buscas import *
from usuarios import *
from registros import *
from atualizardados import *
from remocao import *

dados_usuario = {'Nome de usuário': ['domh'], 'E-mail': ['d@.com'], 'Senha': ['123456789'], 'Tipo de usuário': [1]}

# Produtos e serviços
produto = {'Nome do produto': [], 'Descrição do produto': [], 'Categoria': [], 'Valor': [], 'Quantidade': []}
servico = {'Nome do serviço': [], 'Descrição do serviço': [], 'Categoria': [], 'Profissional': [], 'Valor': [], 'Horário': []}
profissionais = {'Nome do profissional': [], 'Ocupação': [], 'Hora de entrada': [], 'Hora de saída': []}
pets = []
carrinho = []
agenda = []
pets_venda = {'Identificador': [], 'Raça': [], 'Valor': [], 'Quantidade disponível': []}
# Sistema funcionando
print("BEM-VINDO AO PET SERTÃO\nLUGAR DE MUITO AMOR E COMPAIXÃO")

while True:
    menu = int(input('Deseja fazer login ou cadastro?\n1 - Cadastro\t2 - Login\t3 - Sair\n'))
    if menu == 1:
        print('OPÇÃO ESCOLHIDA: CADASTRO')

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

        userRegister(dados_usuario, nomeusuario, emailusuario, senhausuario, tipousuario)
        continue

    elif menu == 2:
        print('OPÇÃO ESCOLHIDA: LOGIN')

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

        userLogin(dados_usuario, emailusuario, senhausuario)
            # break

        for tipo in dados_usuario['Tipo de usuário']:
            if tipo == 1:
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
                            productReg(produto)

                        elif tipo_acao == 2:
                            servReg(servico, profissionais)

                        elif tipo_acao == 3:
                            petsVendaReg(pets_venda)

                    elif opcao_usuario == 2:
                        nomeprodserv = input('Digite o nome do produto, serviço ou pet: ').upper()
                        tipo = int(input('1 - Produto\t2 - Serviço:\n3 - Pets'))
                        if tipo == 1:
                            produtoBusca(produto, nomeprodserv)

                        elif tipo == 2:
                            servicoBusca(servico, nomeprodserv)

                        elif tipo == 3:
                            petsvendaBusca(pets_venda, nomeprodserv)

                    elif opcao_usuario == 3:
                        profissionaisReg(profissionais)

                    elif opcao_usuario == 4:
                        atualizarProfissionais(profissionais)

                    elif opcao_usuario == 5:
                        nomeprodserv = input('Digite o nome do produto: ').upper()
                        tipo = int(input('1 - Produto\t2 - Serviço:\n'))
                        if tipo == 1:
                            atualizarProduto(produto, nomeprodserv)
                            
                        elif tipo == 2:
                            atualizarServico(servico, nomeprodserv)

                        elif tipo == 3:
                            atualizarPetsVenda(pets_venda, nomeprodserv)

                    elif opcao_usuario == 6:
                        nomeprodserv = input('Digite o nome do produto/serviço: ').upper()
                        tipo = int(input('1 - Produto\t2 - Serviço:\n3 - Pet\n'))
                        if tipo == 1:
                            remover(produto)
                            print('ATUALIZAÇÃO FEITA COM SUCESSO!')
                        elif tipo == 2:
                            remover(servico)
                            print('ATUALIZAÇÃO FEITA COM SUCESSO!')
                        elif tipo == 3:
                            remover(pets_venda)
                            print('ATUALIZAÇÃO FEITA COM SUCESSO')

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
            elif tipo == 2:
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

    else:
        print('OPÇÃO INVÁLIDA')
        continue