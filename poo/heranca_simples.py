class Veiculo:
    def __init__(self, cor: str, placa: str, numero_rodas: int) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando motor")
 
    def __str__(self) -> str:
        return f"{self.__class__.__name__} : {'; '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    def __init__(self, cor: str, placa: str, numero_rodas: int, encomenda) -> None:
        super().__init__(cor, placa, numero_rodas)

        self.encomenda = encomenda

    def carrega_encomenda(self):
        return f"{'sim' if self.encomenda == True else 'não' }, carregamos encomenda"

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor: str, placa: str, numero_rodas: int, carregado) -> None:
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
    def estar_carregado(self):
        print(f"{ 'sim' if self.carregado == True else 'Não'}, estou carregado")

    
caminhao = Caminhao("branca", "fgh-562", 8, False)
carro = Carro("vermelho", "def-652", 4)
moto = Motocicleta("Preta", "hij-562", 2,  False )

print(caminhao)
print(carro)
print(moto)

