class Pessoa:
    _total_pessoas = 0

    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        Pessoa._total_pessoas += 1

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18
    @classmethod
    def get_total_pessoas(cls):
        return Pessoa._total_pessoas

# p = Pessoa("Guilherme", 28)
# print(p.nome, p.idade)

print(Pessoa.get_total_pessoas())

p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)
# print(Pessoa.get_total_pessoas(p))

print(p.get_total_pessoas())

p1 = Pessoa("alberto", 20)

print(p.get_total_pessoas())

print(p.e_maior_de_idade(p.idade))
