def userRegister(dados_usuario, nomeusuario, emailusuario, senhausuario, tipousuario):
    dados_usuario['Nome de usuário'].append(nomeusuario)
    dados_usuario['E-mail'].append(emailusuario)
    dados_usuario['Senha'].append(senhausuario)
    dados_usuario['Tipo de usuário'].append(tipousuario)
    
    return dados_usuario

def userLogin(dados_usuario, emailusuario, senhausuario):
    for i in dados_usuario['E-mail']:
        if i == emailusuario:
            for j in dados_usuario['Senha']:
                if j == senhausuario:
                    print('USUÁRIO ENCONTRADO COM SUCESSO!')
                    nome_index = dados_usuario['Nome de usuário'].index(emailusuario)
                    print(f'NOME DE USUÁRIO: {nome_index}\nE-MAIL: {dados_usuario['E-mail'].get(nome_index)}\n')
                    if dados_usuario['Tipo de usuário'].get(nome_index) == 1:
                        print('TIPO DE USUÁRIO: ADM')
                        return 1
                    if dados_usuario['Tipo de usuário'].get(nome_index) == 2:
                        print('TIPO DE USUÁRIO: ADM')
                        return 2