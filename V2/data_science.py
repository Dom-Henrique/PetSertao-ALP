import pandas as pd

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
                
def Abrir_Relatorio():
    with open('Tabelas/DadosUsuario.csv', 'r') as file:
        leitura_arquivo = file.read()
        print(leitura_arquivo)