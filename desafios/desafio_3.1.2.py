import pymongo as pyM
import pprint

client = pyM.MongoClient("mongodb+srv://miller96ti:Dio2024-xgw@cluster0.gfned7f.mongodb.net/?retryWrites=true&w"
                         "=majority&appName=Cluster0")

db = client.desafio #banco desafio
contas = db.contas #coleção contas

clientes_banco = [
    {
      "nome": "John Lennon",
      "cpf": "11122233344",
      "endereco": "251 Menlove Avenue, Liverpool"

    },
    {
      "nome": "Paul McCartney",
      "cpf": "22233344455",
      "endereco": "20 Forthlin Rd, Liverpool"
    },
    {
        "nome": "George Harrison",
        "cpf": "33344455566",
        "endereco": "12 Arnold grove St, Liverpool"
    },
    {
        "nome": "Richard Starkey",
        "cpf": "44455566677",
        "endereco": "9 Madryn St, Liverpool"
    }
    ]

# novos_clientes = contas.insert_many(clientes_banco)
#
# print("\n recuperando documentos inseridos: ")
# # exibe os ids dos documentos inseridos
# # print(novos_clientes.inserted_ids)

# recuperando um cliente específico
# pprint.pprint(contas.find_one({"nome": "George Harrison"}))

# print("Deletando contas")

# db['contas'].drop()

# excluindo um cliente específoco
contas.delete_one({"nome": "Paul McCartney"})

print("\n exibe os documentos restantes:")
for i in contas.find():
    pprint.pprint(i)