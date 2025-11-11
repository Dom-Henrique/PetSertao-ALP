# Cadastrar produto, serviço ou pet
def cadastrar_produto(produto):
    nomeproduto = input('Digite o nome do produto: ').upper()
    categoria_pet = input('Digite o categoria de animal do produto: ').upper()
    produtovalor = float(input('Digite o valor do produto: '))
    qtnd_disponivel = int(input('Digite a quantidade no estoque: '))

    dados_produto = [nomeproduto, categoria_pet, produtovalor, qtnd_disponivel]

    produto.append(dados_produto)
    print('Cadastro bem-sucedido!')