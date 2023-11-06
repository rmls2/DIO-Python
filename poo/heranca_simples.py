class Veiculo:
    def __init__(self, cor: str, placa: str, numero_rodas: int) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

moto = Motocicleta("preta", "abc-256", 2)
print(moto)
moto.ligar_motor()