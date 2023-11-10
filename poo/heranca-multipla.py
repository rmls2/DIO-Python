class Animal:
    def __init__(self, nro_patas) -> None:
        self.nro_patas = nro_patas

    def __str__(self) -> str:
            return f"{self.__class__.__name__} : {'; '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw) -> None:
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    def __str__(self) -> str:
        return "mamifero"

class Ave(Animal):
    def __init__(self, cor_bico, **kw) -> None:
        self.cor_bico = cor_bico
        super().__init__(**kw)
    def __str__(self) -> str:
        return "ave"
    
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, nro_patas) -> None:
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas) 
        
        ## tbm funcionaria se fizéssemos usando **kw
         # def __init__(self, **kw)
           #  super().__init__(**kw) ## tbm funcionaria se fizéssemos usando **kw
        #print(Ornitorrinco.__mro__)
    def __str__(self) -> str:
        return super().__str__()
    
ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="vermelho", cor_bico="azul")
print(ornitorrinco)