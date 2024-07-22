import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://miller96ti:Dio2024-xgw@cluster0.gfned7f.mongodb.net/?retryWrites=true&w"
                         "=majority&appName=Cluster0")
# cria o banco de dados
db = client.test
# cria a coleçao test_collection
collection = db.test_collection

# cria um documento para essa coleção de teste
teste_doc = {
    "name": "teste name",
    "data": datetime.datetime.now(datetime.UTC)
}

# insere esse documento de teste e cria um id para ele
teste_id = collection.insert_one(teste_doc).inserted_id

print(collection)
print(teste_id)
post ={
    "author": "Mike",
    "text": "My first mongodb application based on python",
    "tags": ["MongoDB", "Python3", "Pymongo"],
    "date": datetime.datetime.now(datetime.UTC)
}


# cria a coleção posts
posts = db.posts
# inserindo um documento post e gerando um id para esse documento
post_id = posts.insert_one(post).inserted_id
print(post_id)
print(posts)

# retorna uma lisa com os nomes da coleção
print(db.list_collection_names())
# find_one() = select * from
# printa bonitinho, bem formatado
pprint.pprint(posts.find_one())

# bulk inserts

new_posts = [
    {
        "author": "John Lennon",
        "text": "imagine audpipo",
    },
    {
        "author": "Paul McCartney",
        "text": "letibi",
        "date": datetime.datetime.now(datetime.UTC)
    }
]

# inserir mais de um documento
result = posts.insert_many(new_posts)
print("\n recuperando documentos inseridos: ")
# exibe os ids dos documentos inseridos
print(result.inserted_ids)

# recuperando um author específico
pprint.pprint(posts.find_one({"author": "John Lennon"}))

# deletando o banco de dados
# client.drop_database('test')