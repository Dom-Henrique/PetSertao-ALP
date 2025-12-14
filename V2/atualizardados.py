def atualizarProfissionais(profissionais):
    profissional = input('Nome do(a) profissional: ').upper()
    for nomes in profissionais['Nome do profissional']:
        if nomes == profissional:
            indice = profissionais['Nome do profissional'].index(profissional)
            
            profissionais['Nome do profissional'][indice] = input('Nome do profissional: ').upper()
            profissionais['Ocupação'][indice] = input('Ocupação: ').upper()
            while True:
                profissionais['Hora de entrada'][indice] = int(input('Digite a hora de chegada: '))
                profissionais['Hora de saída'][indice] = int(input('Digite a hora de saída: '))
                if (profissionais['Hora de entrada'][indice] > 6 and profissionais['Hora de entrada'][indice] < 16) and (profissionais['Hora de saída'][indice] > 8 and profissionais['Hora de saída'][indice] < 18):
                    print('ATUALIZAÇÃO FEITA COM SUCESSO!')
                    break
                else:
                    print("FUNCIONAMENTO APENAS DE 6H ÀS 18H\nTENTE NOVAMENTE")
        else:
            print('NÃO ENCONTRADO OU INEXISTENTE')
                        
def atualizarProduto(produto, nomeprodserv):
    for nomes in produto['Nome do produto']:
        if nomes == nomeprodserv:
            indice = produto['Nome do produto'].index(nomes)
            
            produto['Nome do produto'][indice] = input('Digite o nome do produto: ').upper()
            produto['Descrição do produto'][indice] = input('Digite a descrição do produto: ').upper()
            produto['Categoria'][indice] = input('Digite a categoria: ').upper()
            produto['Valor'][indice] = input('Digite o valor: ')
            produto['Quantidade'][indice] = input('Digite a quantidade: ')
            
            print('ATUALIZAÇÃO FEITA COM SUCESSO!')
        else:
            print('NÃO ENCONTRADO OU INEXISTENTE')

def atualizarServico(servico, nomeprodserv):
    for nomes in servico['Nome do serviço']:
        if nomes == nomeprodserv:
            indice = servico['Nome do servico'].index(nomes)
            
            servico['Nome do servico'][indice] = input('Digite o nome do produto: ').upper()
            servico['Descricao do servico'][indice] = input('Digite a descrição: ').upper()
            servico['Categoria'][indice] = input('Digite a categoria: ').upper()
            servico['Valor'][indice] = float(input('Digite o valor do produto: '))
            servico['Horário'][indice] = int(input('Digite o horário: '))
            
            print('ATUALIZAÇÃO FEITA COM SUCESSO!')
        else:
            print('NÃO ENCONTRADO OU INEXISTENTE')

def atualizarPetsVenda(pets_venda, nomeprodserv):
    for id in pets_venda['Identificador']:
        if id == nomeprodserv:
            indice = pets_venda['Identificador'].index(id)
            
            pets_venda['Identificador'][indice] = int(input('ID do pet: '))
            pets_venda['Raça'][indice] = input('Raça do pet: ')
            pets_venda['Valor'][indice] = float(input('Valor do pet: '))
            pets_venda['Quantidade disponível'][indice] = int(input('Quantidade do pet: '))
            
            print('ATUALIZAÇÃO FEITA COM SUCESSO!')
        else:
            print('NÃO ENCONTRADO OU INEXISTENTE')