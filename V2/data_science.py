import pandas as pd
import os

def Usuarios_Info(dados_usuario_df):
    print(dados_usuario_df.describe())
    
    while True:
        print('DESEJA FILTRAR POR ALGUMA CONDIÇÃO?')
        option = int(input('1 - NOMES DE USUÁRIO\n2 - E-MAILS\n3 - NOME ESPECÍFICO\n4 - E-MAIL ESPECÍFICO\n5 - SAIR\n'))
        
        if option == 1:
            print(dados_usuario_df['Nome de usuário'])
            print(dados_usuario_df['Nome de usuário'].describe())
        elif option == 2:
            print(dados_usuario_df['E-mail'])
            print(dados_usuario_df['E-mail'].describe())
        elif option == 3:
            nome_desejado = input('Insira o nome desejado: ')
            if nome_desejado in dados_usuario_df:
                print(dados_usuario_df.loc['Nome de usuário'] == nome_desejado)
                print(dados_usuario_df.loc['Nome de usuário'].describe() == nome_desejado)
        elif option == 4:
            email_desejado = input('Insira o nome desejado: ')
            if email_desejado in dados_usuario_df:
                print(dados_usuario_df.loc['E-mail'] == email_desejado)
                print(dados_usuario_df.loc['E-mail'].describe() == email_desejado)
        elif option == 5:
            break
                
def GerarRelatorio(produto, servico, pets_venda, dados_usuario, profissionais):
    estrutura_dados = input('Relatório desejado: ').lower()
    if estrutura_dados == 'produtos':
        produtosDF = pd.DataFrame(produto)
        produtosDF.to_csv('Tabelas/produtos.csv', index=False)
    elif estrutura_dados == 'serviços':
        servicosDF = pd.DataFrame(servico)
        servicosDF.to_csv('Tabelas/servicos.csv', index=False)
    elif estrutura_dados == 'pets a venda':
        pets_vendaDF = pd.DataFrame(pets_venda)
        pets_vendaDF.to_csv('Tabelas/pets_a_venda.csv', index=False)
    elif estrutura_dados == 'usuários':
        usuariosDF = pd.DataFrame(dados_usuario)
        usuariosDF.to_csv('Tabelas/usuarios.csv', index=False)
    elif estrutura_dados == 'profissionais':
        profissionaisDF = pd.DataFrame(profissionais)
        profissionaisDF.to_csv('Tabelas/profissionais.csv', index=False)
    else:
        print('INDISPONÍVEL')