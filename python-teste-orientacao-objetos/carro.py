from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, cor, qtde_rodas, marca, tanque):
        Veiculo.__init__(self, cor, qtde_rodas, marca, tanque)