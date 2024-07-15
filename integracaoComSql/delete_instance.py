from sqlalchemy.orm import declarative_base, sessionmaker
from config.database import engine
from integracaoComSql.sql_alchemy_aplication import User, Address

# Base = declarative_base()
# Base.metadata.create_all(bind=engine)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # faz a conexão com o banco de dados
session = Session()

try:
    # Deletar todos os registros da tabela Address
    session.query(Address).delete()
    # Deletar todos os registros da tabela User
    session.query(User).delete()

    # Confirmar as transações
    session.commit()
    print("Todos os registros de User e Address deletados com sucesso.")

except Exception as e:
    session.rollback()  # Reverter alterações em caso de erro
    print("Erro ao deletar registros:", e)
finally:
    session.close()
