def userRegister(dados_usuario, nomeusuario, emailusuario, senhausuario, tipousuario):
    dados_usuario['Nome de usuário'].append(nomeusuario)
    dados_usuario['E-mail'].append(emailusuario)
    dados_usuario['Senha'].append(senhausuario)
    dados_usuario['Tipo de usuário'].append(tipousuario)
    
    return dados_usuario

def userLogin(dados_usuario, emailusuario, senhausuario):
    for i in dados_usuario['E-mail']:
        if i == emailusuario:
            print('E-MAIL ENCONTRADO COM SUCESSO!')
            for j in dados_usuario['Senha']:
                if j == senhausuario:
                    print('USUÁRIO ENCONTRADO COM SUCESSO!')
                    nome_index = dados_usuario['E-mail'].index(i)
                    print(f'NOME DE USUÁRIO: {dados_usuario['Nome de usuário'][nome_index]}\nE-MAIL: {emailusuario}\n')
                    if dados_usuario['Tipo de usuário'][nome_index] == 1:
                        print('TIPO DE USUÁRIO: ADM')
                        return 1
                        break
                    if dados_usuario['Tipo de usuário'][nome_index] == 2:
                        print('TIPO DE USUÁRIO: ADM')
                        return 2
                        break
        else:
            print('E-MAIL NÃO ENCONTRADO')