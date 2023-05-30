#quantidade_pessoas = int(input('Digite aqui a quantidade de pessoas que virão à sua festa: '))
#contador = 0

#o programa abaixo contém erro: somente grava na memória o nome do último convidado
'''
while contador < quantidade_pessoas:
    lista_pessoas = []
    pessoa = input('Digite aqui o nome de seu convidado(a): ')
    lista_pessoas.append(pessoa)
    contador +=1

print(lista_pessoas)
'''

#programa certo: que cria uma lista e atualiza ela com todos os nomes, abaixo:
quantidade_pessoas = int(input('Digite aqui o número de pessoas que virão à sua festa: '))
contador = 0
lista_pessoas = []

while contador < quantidade_pessoas:
    pessoa = input('Digite aqui o nome de seu convidado(a): ')
    lista_pessoas.append(pessoa)
    contador = contador + 1

print(lista_pessoas)
