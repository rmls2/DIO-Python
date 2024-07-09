import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, ForeignKey, String, create_engine, inspect

Base = declarative_base()


class User(Base):
    __tablename__: str = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    full_name = Column(String)

    address = relationship(

        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id = {self.id}, name = {self.name})"


class Address(Base):
    __tablename__: str = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship(
        "User", back_populates="address"
    )

    def __repr__(self):
        return f"Adress(id = {self.id}, email_adress = {self.email_address})"


# conexão com o banco de dados
engine = create_engine("sqlite://")

# depreciado - será removido em uma release futura
# print(engeine.table_names())

# criando as bases como tabelas no banco de dados
Base.metadata.create_all(engine)

# investiga o esquema do banco de dados - função que permite tirar informações sobre nossa conexão
inspetor_engine = inspect(engine)

print(inspetor_engine.get_table_names())
print(inspetor_engine.has_table("cata"))

# quabdo não definimos o nome do nosso esquema(banco de dados) por default ele se chamará "main"
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    juliana = User(
        name="Juliana",
        full_name="Juliana Mascarenhas",
        address=[Address(email_address="Julianam@email.com")]
    )

    sandy =  User(
        name="Sandy",
        full_name="Sandy Cardoso",
        address=[Address(email_address="sandy@email.com"), Address(email_address="sandyc@email.com")]
    )

    patrick = User(name="Patrick", full_name="Patrick Cardoso")

    # enviando para o BD (persistência de dados)
    session.add_all([juliana, sandy, patrick])

    session.commit()

