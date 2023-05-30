print('Escolha dentre as opções abaixo: \n1. Registrar Nota\n2. Registrar Aluno\n3. Registrar Matéria\n4. Informar Problema\n')
opcao = input('Escolha sua opção: ')

if opcao == '1':
    print('OK, vamos registrar a Nota!')
elif opcao == '2':
    print('OK, vamos resitrar o novo Aluno!')
elif opcao == '3':
    print('OK, vamos registrar a nova Matéria!')
elif opcao == '4':
    print('OK, informe seu problema abaixo:\n')
    problema = input()
    print('\nConfirme se esse foi o seu relato para o problema: ' , problema)
    print('\nPodemos enviar o seu relato? Digite 1 para "SIM" ou 2 para "NÃO"\n')
    resposta_problema = input('Digite aqui: ')
    if resposta_problema == 1:
        print('OK, enviamos seu relato para o setor de Suporte')
    elif resposta_problema == 2:
        print('OPS! Parece que houve algum problema!')
    