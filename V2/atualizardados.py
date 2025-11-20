def atualizarProfissionais(profissionais):
    profissional = input('Nome do(a) profissional: ').upper()
    for j in profissionais.values():
        for i in j:
            if profissionais['Nome do profissional'][i] == profissional:
                profissionais['Nome do profissional'][i] = input('Nome do profissional: ').upper()
                profissionais['Ocupação'][i] = input('Ocupação: ').upper()
                while True:
                    profissionais['Nome do profissional'][i] = int(input('Digite a hora de chegada: '))
                    profissionais['Nome do profissional'][i] = int(input('Digite a hora de saída: '))
                    if (profissionais['Hora de entrada'][i] > 6 and profissionais['Hora de entrada'][i] < 16) and (profissionais['Hora de saída'][i] > 8 and profissionais['Hora de saída'][i] < 18):
                        break
                    else:
                        print("FUNCIONAMENTO APENAS DE 6H ÀS 18H\nTENTE NOVAMENTE")
                        
def atualizarProduto(produto, nomeprodserv):
    for produtinhos in produto.values():
        for i in produtinhos:
            if nomeprodserv == produto['Nome do produto'][i]:
                produtinhos[0] = input('Digite o nome do produto: ').upper()
                produtinhos[1] = input('Digite a categoria: ').upper()
                produtinhos[2] = float(input('Digite o valor do produto: '))
                produtinhos[3] = int(input('Digite a quantidade disponível: '))

def atualizarServico(servico, nomeprodserv):
    for servicinhos in servico.values():
        for i in servicinhos:
            if nomeprodserv == servico['Nome do produto'][i]:
                servicinhos[0] = input('Digite o nome do produto: ').upper()
                servicinhos[1] = input('Digite a categoria: ').upper()
                servicinhos[2] = float(input('Digite o valor do produto: '))
                servicinhos[3] = int(input('Digite a quantidade disponível: '))

def atualizarPetsVenda(pets_venda, nomeprodserv):
    for petsinhos in pets_venda.values():
        for i in petsinhos:
            if nomeprodserv == pets_venda['Nome do produto'][i]:
                petsinhos[0] = input('Digite o nome do produto: ').upper()
                petsinhos[1] = input('Digite a categoria: ').upper()
                petsinhos[2] = float(input('Digite o valor do produto: '))
                petsinhos[3] = int(input('Digite a quantidade disponível: '))