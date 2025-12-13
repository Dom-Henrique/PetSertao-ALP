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