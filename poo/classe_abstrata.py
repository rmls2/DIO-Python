from abc import ABC, abstractmethod

class ControleRemoto(ABC):
   
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def desligar(self):
        print("Desligando")
        print("tv dsligada")
        
    def ligar(self):
        print("Ligando")
        print("tv ligada")

    @property
    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def desligar(self):
        print("Desligando")
        print("Ar dsligada")
        
    def ligar(self):
        print("Ligando")
        print("Ar ligada")

    @property
    def marca(self):
        return "Philco"
    
controle = ControleTV()

controle.desligar()
controle.ligar()
print(controle.marca)

controleAr = ControleArCondicionado()

controleAr.desligar()
controleAr.ligar()
print(controleAr.marca)