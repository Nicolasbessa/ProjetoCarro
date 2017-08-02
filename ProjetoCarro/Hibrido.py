from Carro import Carro

class Hibrido(Carro):
    def __init__(self, cor, modelo, ano, carregarBateria):
        super(Carro, self).__init__(cor, modelo, ano)
        self.carregarBateria = carregarBateria


