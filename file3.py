
#mongodb+srv://Ynifa:<password>@cluster0.3at7v.mongodb.net/<dbname>?retryWrites=true&w=majority
import pymongo
from configparser import ConfigParser
config = ConfigParser()
file = "config.ini"
config.read(file)
params = dict(config["params"])

cluster = pymongo.MongoClient(params["mongdb_credentials"])
db = cluster["test"]

collection = db["test"]

# Add stuff to db
#post = {"_id":1,"name":"Yassine","score":5}
post = {"_id":6,"name":"Amine","score":12}
# collection.insert_one(post)

#To insert many post
data = [{"_id": 2,"name":"Lam","score":20},{"_id": 3,"name":"kam","score":202}]
#collection.insert_many(data)


"""Find information"""
result = collection.find({"name":"Amine"})
#print(result)
for x in result:
	print(x)

	
"""search using a multiple field"""
result = collection.find({"name":"Amine","score":12})
for x in result:
	print(x)

"""Find one result""" 
result = collection.find_one({"name":"Amine"})
print(result)

"""find without criteria, it returns everything"""
result = collection.find({})
for x in result:
	print(x)

"""To delete  one element"""
result = collection.delete_one({"_id":1})

"""To delete many element"""
result = collection.delete_many({"_id":,"_id"})

"""update"""
result = collection.update_one({"_id":2},{"$set":{"name":"Lamnouar"}})
"""add field"""
result = collection.update_one({"_id":2},{"$set":{"lastname":"nifa"}})

# Count the number of documents
post_count = collection.count_documents({"name":"Yassine"})
print(post_count)
