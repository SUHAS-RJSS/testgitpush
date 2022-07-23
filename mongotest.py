import pymongo


client = pymongo.MongoClient("mongodb+srv://ineuron:suhas1234@cluster0.wjp2d.mongodb.net/?retryWrites=true&w=majority")
db = client.test


print(db)


d = {
    'name' : 'suhas',
    'email':'suhassr26@gmail.com',
    'surname':'rjss'
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
