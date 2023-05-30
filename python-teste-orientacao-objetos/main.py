#importando do arquivo veiculo a Classe Veiculo (para construir meu objeto)
from veiculo import Veiculo
from carro import Carro

# caminhao_verde = Veiculo('verde', '6', 'fiat', '300')
# print('Cor: ', caminhao_verde.cor)
# print('Tanque (litros): ', caminhao_verde.tanque)

# carro_preto1 = Veiculo('preto', '4', 'chevrolet', '55')
# carro_preto2 = Veiculo('preto', '4', 'volkswagen', '40')
# onibus_escolar = Veiculo('amarelo', '6', 'mercedes', '150')

from cliente import Cliente
cliente1 = Cliente('Zé', '35', 'motorista', '5000')
print('Nome do cliente: ', cliente1.nome)
