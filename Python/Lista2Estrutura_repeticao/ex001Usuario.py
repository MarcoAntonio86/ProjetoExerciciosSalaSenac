usuario = input('Informe seu nome: ')
senha = input('Informe sua senha: ')

while senha == usuario:
    print('Senha incorreta, nome de usúario e senha não podem ser o mesmo !')
    usuario = input('Informe seu nome: ')
    senha = input('Informe sua senha: ')
print('Bem vindo {}'.format(usuario))