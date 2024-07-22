""" criamos esse script porque no outro script ao executar o mesmo código, estaremos crioando os mesmos documentos a cada execução"""

import pprint

import pymongo
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://miller96ti:Dio2024-xgw@cluster0.gfned7f.mongodb.net/?retryWrites=true&w"
                         "=majority&appName=Cluster0")

db = client.test
posts = db.posts

"""posts.find() me retorna um cursor (seja la o que seja isso, mas é um iterável) e ao percorrê-lo temos accesso a todos os 
documentos da coleção posts"""

print("\n recuperando informações por ordenação de data: ")
for post in posts.find().sort("date"):
    pprint.pprint(post)

print("\ncontando a quantidade de documentos: ")
pprint.pprint(posts.count_documents({}))
print("\ncontando documentos por autor específico: ")
pprint.pprint(posts.count_documents({"author": "Paul McCartney"}))
pprint.pprint(posts.count_documents({"tags": "Python3"}))

result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique=True)

# print(sorted(list(db.profiles.index_information())))

# vai listar todas as coleções que temos no nosso banco de dados
for i in db.list_collection_names():
    print(i)

profiles_doc = [
    {
        "author": 1,
        "livros": ["Ocodigo da Vinci", "Inferno", "Fortaleza Digital"]},
    {
        "author": 2,
        "Livros": ["Memoras Póstumas de Bras Cubas", "Helena"]
    }
]
# profiles_result = db.profiles.insert_many(profiles_doc)
profiles = db.profiles
# print("\ntestedsds: ")
# for i in profiles.find():
#     pprint.pprint(i)

# assim exclui todos os documentos de uma coleção
# db['posts'].drop()

# assim exclui a coleção toda
# posts.drop()

profiles.drop()

# vai listar todas as coleções que temos no nosso banco de dados
for i in db.list_collection_names():
    print(i)

print(profiles.find_one({}))

# excluindo um documento específico
profiles.delete_one({"author": 1})

print("\ncoleções: ")

# excluir todas as coleções
for collection in db.list_collection_names():
    print("tchau, coleção: ", collection)
    col = db.collection
    col.drop()

print("vazio:", db.list_collection_names())

# deletando o banco de dados
client.drop_database('test')
