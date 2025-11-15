def produtoBusca(produto, nomeprodserv):
    for produtinhos in produto:
        if nomeprodserv == produtinhos[0]:
            print(f'Dados do produto: {produto['Nome do produto'][produtinhos]}\n{produto['Descrição do produto'][produtinhos]}\n{produto['Categoria'][produtinhos]}\n{produto['Valor'][produtinhos]}')
        else:
            print('NÃO ENCONTRADO')
                
def servicoBusca(servico, nomeprodserv):
    for servicinhos in servico['Nome do serviço']:
        if nomeprodserv == servicinhos[0]:
            print(f'Dados do Serviço: {servico['Nome do servico'][servicinhos]}\n{servico['Descrição do servico'][servicinhos]}\n{servico['Categoria'][servicinhos]}\n\n{servico['Valor'][servicinhos]}\n{servico['Quantidade'][servicinhos]}')
        else:
            print('NÃO ENCONTRADO')
            
def petsvendaBusca(pets_venda, nomeprodserv):
    for petsinhos in pets_venda:
        if petsinhos[0] == nomeprodserv:
            print(f'Dados do pet: {pets_venda[petsinhos]}')
        else:
            print('NÃO ENCONTRADO')