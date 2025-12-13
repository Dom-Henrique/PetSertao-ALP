from buscas import *
from usuarios import *
from registros import *
from atualizardados import *
from remocao import *
from data_science import *
from compras import *
#from capturar_rosto import *
import pandas as pd
import speech_recognition as ar
from random import randint
import os
from time import sleep

dados_usuario = {'Nome de usuário': ['domh'], 'E-mail': ['d@.com'], 'Senha': ['123456789'], 'Tipo de usuário': [1], 'ID': ['453740']}

# Produtos e serviços
produto = {'Nome do produto': [], 'Descrição do produto': [], 'Categoria': [], 'Valor': [], 'Quantidade': []}
servico = {'Nome do serviço': [], 'Descrição do serviço': [], 'Categoria': [], 'Profissional': [], 'Valor': [], 'Horário': []}
profissionais = {'Nome do profissional': [], 'Ocupação': [], 'Hora de entrada': [], 'Hora de saída': []}
pets = []
carrinho = []
agenda = []
pets_venda = {'Identificador': [40028922], 'Raça': ['canina'], 'Valor': [10], 'Quantidade disponível': [50]}
# Tabelas utilizando Pandas

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
        
        print('GERANDO O SEU ID...')
        sleep(2)
        id_usuario = randint(100000, 999999)
        print(f'ID DE {nomeusuario}: {id_usuario}')

        tipousuario = int(input('Qual o seu tipo de usuário?\n1 - Administrador\t2 - Cliente\n'))

        userRegister(dados_usuario, nomeusuario, emailusuario, senhausuario, tipousuario, id_usuario)
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
                                                "8 - Gerar relatório\n"
                                                "9 - Sair\n"))

                    if opcao_usuario == 1:
                        tipo_acao = int(input("1 - Produto 2 - Serviço 3 - Pet\n"))
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
                        tipo = int(input('1 - Produto\t2 - Serviço\t3 - Identificador:\n'))
                        if tipo == 1:
                            nomeprodserv = input('Digite o nome do produto: ').upper()
                            atualizarProduto(produto, nomeprodserv)
                            
                        elif tipo == 2:
                            nomeprodserv = input('Digite o nome do produto: ').upper()
                            atualizarServico(servico, nomeprodserv)

                        elif tipo == 3:
                            nomeprodserv = int(input('Digite o nome do produto: '))
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
                        Usuarios_Info(dados_usuario_df)
                        
                    elif opcao_usuario == 8:
                        if os.path.exists('Tabelas'):
                            pass
                        else:
                            os.mkdir('Tabelas')
                        GerarRelatorio(produto, servico, pets_venda, dados_usuario, profissionais)
                    elif opcao_usuario == 9:
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
                        cadastrarMeuPet(pets)

                    # comprar produto
                    elif opcao == 2:
                        while True:
                            produtos_cad = len(produto)

                            if produtos_cad == 0:
                                print('LISTA DE PRODUTOS VAZIA\nAGUARDE PARA MAIS NOVIDADES!')
                                break
                            else:
                                comprar_produto(produto, carrinho)

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