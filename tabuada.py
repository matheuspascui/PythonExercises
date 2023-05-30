print('Este é nosso programa que calcula a tabuada de um número informado.')
numero_tabuada = int(input('Informe o número que deseja saber a tabuada: '))
limite_tabuada = int(input('Informe o limite da tabuada (até que número deseja saber a tabuada): '))

for numero in range(limite_tabuada):
    print(numero * numero_tabuada)
