def comprar_produto(produto,carrinho):
    for p in produto.values():
        print(f'Produto: {p[0]}\nCategoria: {p[1]}\nPreço: R${p[2]}\nQuantidade disponível: {p[3]}\n')

    escolha = input('\nDigite o nome do produto que deseja comprar\nDigite "SAIR" para sair\n> ').upper()

    produto_encontrado = False
    for p in produto:
        if p[0] == escolha:
            carrinho.append(p)
            produto_encontrado = True
            print('ADICIONADO AO CARRINHO!')

    if not produto_encontrado:
        print('PRODUTO NÃO ENCONTRADO')

    return carrinho

def cadastrarMeuPet(pets):
    nome_pet = input('Nome do pet?: ').upper()
    especie = input('Espécie do pet?: ').upper()
    raca = input('Raça do pet?: ').upper()
    idade = int(input('quantos anos tem o pet?: '))
    nome_dono = input('Nome do dono?: ').upper()

    pets['Nome'].append(nome_pet)
    pets['Espécie'].append(especie)
    pets['Raça'].append(raca)
    pets['Idade'].append(idade)
    pets['Dono'].append(nome_dono)

    print('\nPET CADASTRADO COM SUCESSO!\n')

    return pets

def mostrar_servicos(servico):
    while True:
        if len(servico) == 0:
            print('LISTA DE SERVIÇOS VAZIA. AGUARDE PARA MAIS NOVIDADES!')
            break
        else:
            for m in servico['nome do serviço']:
                print(f'Serviço: {m[0]}\nPreço: R${m[1]}\nHorário disponível:{m[2]}')

            escolha = input("\nDigite o nome do serviço que deseja contratar (ou 'SAIR' para sair): ").upper()
            
            if escolha == 'SAIR':
                break

            hora_escolha = int(input('Digite a hora que deseja realizar o serviço: '))
            
            encontrado = False
            for n in servico['nome do serviço']:
                if n[0] == escolha:
                    if int(n[2]) <= hora_escolha:
                        print('Serviço agendado com sucesso!')
                        encontrado = True
                        break
                    else:
                        print('HORÁRIO INDISPONÍVEL')
                        encontrado = True
                        break
            
            if not encontrado:
                print('Serviço não encontrado ou horário inválido. Tente novamente.')
             
def comprar_pet(pets_venda, carrinho):
     if len(pets_venda) == 0:
                 print('Nenhum pet disponível')
                  return

                 especie = input('Espécie que você procura: ').upper()
                 achou = False

            for p in pets_venda['pets disponiveis']:
            if p[1] == especie and p[3] > 0:
            print('Identificador:', p[0])
            print('Espécie:', p[1])
            print('Preço:', p[2])
            print('Quantidade:', p[3])
            print()
            achou = True

            if achou == False:
            print('Nenhum pet dessa espécie disponível')
            return

            codigo = int(input('Digite o código do pet que deseja comprar: '))
             comprado = False

            for p in pets_venda:
            if p[0] == codigo and p[3] > 0:
               carrinho.append(p)
             p[3] = p[3] - 1
             print('Compra realizada com sucesso!')
             comprado = True

            if comprado == False:
              print('Código inválido ou pet sem estoque')

def mostrar_servicos(servico):
    while True:
        if len(servico) == 0:
            print('LISTA DE SERVIÇOS VAZIA. AGUARDE PARA MAIS NOVIDADES!')
            break
        else:
            for m in servico['qual serviço agendar?']:
                print(f'Serviço: {m[0]}\nPreço: R${m[1]}\nHorário disponível: {m[2]}')

            escolha = input("\nDigite o nome do serviço que deseja contratar (ou 'SAIR' para sair): ").upper()
            
            if escolha == 'SAIR':
                break

            hora_escolha = int(input('Digite a hora que deseja realizar o serviço: '))
            
            encontrado = False
            for n in servico:
                if n[0] == escolha:
                    if int(n[2]) <= hora_escolha:
                        print('Serviço agendado com sucesso!')
                        encontrado = True
                        break
                    else:
                        print('HORÁRIO INDISPONÍVEL')
                        encontrado = True
                        break
            
            if not encontrado:
                print('Serviço não encontrado ou horário inválido. Tente novamente.')
        



 