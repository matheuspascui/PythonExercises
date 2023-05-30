print('Olá! Essa é a nossa tela de login. Você já possui cadastro em nosso sistem?')
possui_cadastro = input('1. Possuo Cadastro\n2. Não possuo cadastro\nSelecione sua opção: ')
if possui_cadastro == '1':
    print('OK! Vamos então logar no sistema.')
    nome_usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    dados_usuario = nome_usuario + senha
    print('\n\n', dados_usuario, '\n\n')
elif possui_cadastro == '2':
    print('OK! Vamos então criar seu usuário.')
    novo_usuario = input('Digite aqui seu nome de usuário: ')
    nova_senha = input('Digite aqui sua senha: ')
    dados_novo_usuario = novo_usuario + nova_senha
    print('\n\n', dados_novo_usuario, '\n\n')

print('Obrigado por usar nosso sistema! :)')


# user = input('Digite aqui seu nome de usuário: ')
# print(user)
# password = input('Digite aqui sua senha: ')