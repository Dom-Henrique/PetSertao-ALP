def productReg(produto):
    nomeproduto = input('Nome do produto: ').upper()
    descproduto = input('Descrição do produto: ')
    categoria_pet = input('Categoria de animal do produto: ').upper()
    produtovalor = float(input('Valor do produto: '))
    qtnd_disponivel = int(input('Quantidade no estoque: '))

    produto['Nome do produto'].append(nomeproduto)
    produto['Descrição do produto'].append(descproduto)
    produto['Categoria'].append(categoria_pet)
    produto['Valor'].append(produtovalor)
    produto['Quantidade'].append(qtnd_disponivel)
    
    print('CADASTRO FEITO COM SUCESSO!')
    
    return produto
    
def servReg(servico, profissionais):
    nomeservico = input('Digite o nome do serviço: ').upper()
    descservico = input('Dê uma descrição do serviço: ')
    categoria_pet = input('Digite o categoria de animal do produto: ').upper()
    
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
                            servico['Nome do serviço'].append(nomeservico)
                            servico['Descrição do serviço'].append(descservico)
                            servico['Categoria'].append(categoria_pet)
                            servico['Profissional'].append(profissional)
                            servico['Valor'].append(servicovalor)
                            servico['Horário'].append(hora_func)
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
    
    print('CADASTRO FEITO COM SUCESSO!')
    
    return servico
    
def petsVendaReg(pets_venda):
    identificador = int(input('Identificador do pet: '))
    raca_pet = input('Raça do pet: ').upper()
    valor_pet = float(input('Preço: '))
    qtnd_disponivel = int(input('Quantidade disponível: '))
    
    pets_venda['Identificador'].append(identificador)
    pets_venda['Raça'].append(raca_pet)
    pets_venda['Valor'].append(valor_pet)
    pets_venda['Quantidade Disponível'].append(qtnd_disponivel)
    
    print('CADASTRO FEITO COM SUCESSO!')
    
    return pets_venda
    
def profissionaisReg(profissionais):
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
            
    profissionais['Nome do profissional'].append(nomeprof)
    profissionais['Ocupação'].append(opcupacao)
    profissionais['Hora de entrada'].append(hora_prof_init)
    profissionais['Hora de saída'].append(hora_prof_final)
    
    print('CADASTRO FEITO COM SUCESSO!')