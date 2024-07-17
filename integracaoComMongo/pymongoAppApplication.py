import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://miller96ti:<password>@cluster0.gfned7f.mongodb.net/?retryWrites=true&w"
                         "=majority&appName=Cluster0")
db = client.test
collection = db.test_collection
print(collection)
