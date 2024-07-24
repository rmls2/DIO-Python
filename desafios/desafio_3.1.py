from sqlalchemy.orm import (declarative_base, Mapped, mapped_column, relationship, Session)
from typing import List
from sqlalchemy import (String, ForeignKey, create_engine, inspect, select)

Base = declarative_base()


# Criação das tabelas usando orm
class Cliente(Base):

    __tablename__ = "cliente"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    endereco: Mapped[str] = mapped_column(String)

    contas: Mapped[List["Conta"]] = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"


class Conta(Base):

    __tablename__ = "conta"

    id: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str] = mapped_column(String(20), nullable=False)
    agencia: Mapped[str] = mapped_column(String(7), nullable=False)
    numero: Mapped[int] = mapped_column(nullable=False)
    saldo: Mapped[float] = mapped_column(nullable=False, default=0.0)
    id_cliente: Mapped[int] = mapped_column(ForeignKey("cliente.id"), nullable=False)

    cliente: Mapped["Cliente"] = relationship(back_populates="contas")

    def __repr__(self):
        return f"Conta(id={self.id}, tipo[{self.tipo}, agencia={self.agencia}, numero={self.numero}, saldo={self.saldo}, id_cliente={self.id_cliente}"


# conexao com o banco de dados - criação do DB do desafio
SQLALCHEMY_DATABASE_URL = "sqlite:///./desafio.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# criando uma inspector
inspetor_engine = inspect(engine)
# retorna vazio porque as tabelas ainda não foram criadas
print(inspetor_engine.get_table_names())

# criando nosso esquema no banco de dados
Base.metadata.create_all(bind=engine)

# inserindo dados na nossa tabela - tornando os dados permanentes

# with Session(engine) as session:
#     john_lennon = Cliente(
#         nome="John Wiston Lennon",
#         cpf="11122233344",
#         endereco="251 Menlove Avenue, Liverpool",
#         contas=[Conta(tipo="Conta corrente", agencia="Bank of Liverpool", numero=1234 , saldo=1500.00),
#                 Conta(tipo="Conta popança", agencia="Bank of New York", numero=1235 , saldo=500.00)]
#         )
#
#     paul_McCartney = Cliente(
#         nome="James Paul McCartney",
#         cpf="22233344455",
#         endereco=" 20 Forthlin Rd, Liverpool",
#         contas=[Conta(tipo="Conta corrente", agencia="Bank of Liverpool", numero=2345, saldo=1700.00)]
#        )
#
#     george_harrison = Cliente(
#         nome="George Harrison",
#         cpf="33344455566",
#         endereco=" 12 Arnold grove St, Liverpool",
#         contas=[Conta(tipo="Conta corrente", agencia="Bank of Liverpool", numero=3456, saldo=1800.00),
#                 Conta(tipo="Conta popança", agencia="Bank of Los Angels", numero=3457 , saldo=300.00)]
#        )
#
#     ringo_star = Cliente(
#         nome="Richard Starkey",
#         cpf="44455566677",
#         endereco="9 Madryn St, Liverpool",
#         contas=[Conta(tipo="Conta corrente", agencia="Bank of Liverpool", numero=4567, saldo=2000.00),
#                 Conta(tipo="Conta popança", agencia="Bank of Los Angels", numero=4568 , saldo=200.00)]
#        )
#
#     session.add_all([john_lennon, paul_McCartney, george_harrison, ringo_star])
#
#     session.commit()

# realizando consultas para recuperar dados

# select where
stmt = select(Cliente).where(Cliente.nome.in_(['John Wiston Lennon', 'Richard Starkey']))

session = Session(engine)
for user in session.scalars(stmt):
    print(user)

# recuperando o nome e o cpf da primeira instância da tabela cliente
row = session.execute(select(Cliente.nome, Cliente.cpf)).first()
print(row)

# select com join

stmt_join = (
    select(Conta)
    .join(Conta.cliente)
    .where(Cliente.nome == "James Paul McCartney")
    )

for user in session.scalars(stmt_join):
    print(user)

# alterando um dado da instância do "George Harrison"

stmt_alter = select(Cliente).where(Cliente.nome == "George Harrison")
george = session.scalars(stmt_alter).one()

george.contas.append(Conta(tipo="Conta corrente", agencia="Bank of London", numero=3458))

session.commit()