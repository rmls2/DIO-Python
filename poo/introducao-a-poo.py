#Criando e instanciando nossa primeira classe em python

class Bicicleta: 
    def __init__(self, cor, modelo, ano, valor) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 

    def buzinar(self):
        print("BiBi!!!")

    def parar(self, freiar):
        if freiar:
            print("para!")

    def correr(self, correr):
        if correr:
            print("corre!")

    def __str__(self) -> str:
    
        return f"{self.__class__.__name__} : {' - '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

bike = Bicicleta("vermelho", "caloi", 2010, 1000.00)

# print(bike.parar(True))

Bicicleta.buzinar(bike) #é possível chamar um metodo de uma função chamando direto pela classe e passando o objeto como argumento


## printando um objeto 

print(bike.correr(False))

# ao printar um objeto exibimos algo desse tipo: <__main__.Bicicleta object at 0x7ff37dd936a0> que não carrega tanta informação 
# por isso é possível add um metodo str() para ao fazer o print de um objeto ser exibido informações sobre os atributos do objeto.  
#
#    add:   def __str__(self) -> str:
#               return f"{self.__class__.__name__} : {'; '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


print(bike.__str__())