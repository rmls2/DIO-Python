import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, ForeignKey, String, inspect, select, func
from config.database import engine

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


# investiga o esquema do banco de dados - função que permite tirar informações sobre nossa conexão
inspetor_engine = inspect(engine)

print(inspetor_engine.get_table_names())
print(inspetor_engine.has_table("user_account"))

# quando não definimos o nome do nosso esquema(banco de dados) por default ele se chamará "main"
print(inspetor_engine.default_schema_name)

# Criação do esquema no banco de dados
Base.metadata.create_all(bind=engine)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # faz a conexão com o banco de dados
session = Session()

# Adicionando tabelas de usuario
juliana = User(
    name="Juliana",
    full_name="Juliana Mascarenhas",
    address=[Address(email_address="Julianam@email.com")]
)

sandy = User(
    name="Sandy",
    full_name="Sandy Cardoso",
    address=[Address(email_address="sandy@email.com"), Address(email_address="sandyc@email.com")]
)

patrick = User(name="Patrick", full_name="Patrick Cardoso")

try:
    session.add_all([juliana, sandy, patrick])
    session.commit()
except Exception as e:
    session.rollback()
    print("Erro ao adicionar usuários:", e)
finally:
    session.close()

# Consultas usando where
print("\nRecuperando usuário a partir de uma condição de filtragem - where")
try:
    session = Session()
    statement_user = select(User).where(User.name.in_(['Juliana', 'Sandy']))
    for user in session.scalars(statement_user):
        print(user)
finally:
    session.close()

print("\nRecuperando endereços de email de Sandy:")
try:
    session = Session()
    statement_address = select(Address).where(Address.user_id == 2)
    for address in session.scalars(statement_address):
        print(address)
finally:
    session.close()

# Consultas usando order by
print("\nConsultas ordenadas por nome (descendente):")
try:
    session = Session()
    order_statement = select(User).order_by(User.name.desc())
    for user in session.scalars(order_statement):
        print(user)
finally:
    session.close()

# Consulta usando join
print("\nJoin:")
try:
    session = Session()
    join_statement = select(User.full_name, Address.email_address).join_from(Address, User)
    for result in session.execute(join_statement):
        print(result)
finally:
    session.close()

# Estabelecendo a conexão com o banco de dados
connection = engine.connect()
try:
    results = connection.execute(join_statement).fetchall()
    print("\nTrazendo o join de fato:")
    for result in results:
        print(result)
finally:
    connection.close()

# Usando a função count para contar instâncias
print("\nTotal de instâncias de user:", end=' ')
try:
    session = Session()
    count_statement = select(func.count('*')).select_from(User)
    for result in session.scalars(count_statement):
        print(result)
finally:
    session.close()

# deletando uma instância da table user



# jeito da dio, sem exibir o banco de dados
# conexão com o banco de dados
# engine = create_engine("sqlite:///")

# depreciado - será removido em uma release futura
# print(engeine.table_names())

# criando as bases como tabelas no banco de dados
# Base.metadata.create_all(engine)


# investiga o esquema do banco de dados - função que permite tirar informações sobre nossa conexão
# inspetor_engine = inspect(engine)

# print(inspetor_engine.get_table_names())
# print(inspetor_engine.has_table("user_account"))

# quando não definimos o nome do nosso esquema(banco de dados) por default ele se chamará "main"
# print(inspetor_engine.default_schema_name)

# jeito da DIO
# with Session(engine) as session:

# juliana = User(
#     name="Juliana",
#     full_name="Juliana Mascarenhas",
#     address=[Address(email_address="Julianam@email.com")]
# )
#
# sandy = User(
#     name="Sandy",
#     full_name="Sandy Cardoso",
#     address=[Address(email_address="sandy@email.com"), Address(email_address="sandyc@email.com")]
# )
#
# patrick = User(name="Patrick", full_name="Patrick Cardoso")
#
# session.add_all([juliana, sandy, patrick])
# session.commit()
#
# # jeito da DIO
# # enviando para o BD (persistência de dados)
# # session.add_all([juliana, sandy, patrick])
# #
# # session.commit()
#
# # consultas usando where
# print("\nrecuperando usuário a partir de uma condição de filtragem - where")
# statment_user = select(User).where(User.name.in_(['Juliana', 'Sandy']))
#
# for user in session.scalars(statment_user):
#     print(user)
#
# print("\nrecuperando endereços de email de sandy:")
#
# statment_address = select(Address).where(Address.user_id.in_([2]))
#
# for address in session.scalars(statment_address):
#     print(address)
#
# # consultas usando order by
#
# order_statement = select(User).order_by(User.name.desc())
# print("")
# for i in session.scalars(order_statement):
#     print(i)
# print(session.scalars(order_statement))
# # consulta usando  join
#
# join_statment = select(User.full_name, Address.email_address).join_from(Address, User)
#
# print("\nJoin:")
#
# for result in session.scalars(join_statment):
#     print(result)
#
# # printa como é a consulta de fato
# print(join_statment)
#
# # estabelece a conexão com o banco de dados
# connection = engine.connect()
#
# results = connection.execute(join_statment).fetchall()
# print("\ntrazendo o join de fato:")
# for result in results:
#     print(result)
#
# # usando a função count para contar instancias
#
# count_statement = select(func.count('*')).select_from(User)
# print("\nTotal de instancias de user:", end=' ')
#
# for result in session().scalars(count_statement):
#     print(result)
