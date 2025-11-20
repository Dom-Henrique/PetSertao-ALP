def remover(banco_dados, nome_prodserv):
    if banco_dados.keys()[0][i] == nome_prodserv:
        for dados in banco_dados.values():
            for i in dados:
                dados.pop(i)