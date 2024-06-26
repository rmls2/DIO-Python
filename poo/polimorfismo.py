class Passaro:

    def voar(self):
        print("voando")

class Pardal(Passaro):
    
    def voar(self):
        super().voar()
    

class Avestruz(Passaro):
    
    def voar(self):
        print('avestruz não voa')


def voador(objeto: object):  ##é uma função polimórfica, a saida vai depender do objeto estanciado
    return objeto.voar()


obj1 = Pardal()
obj2 = Avestruz()

voador(obj1)
voador(obj2)
    