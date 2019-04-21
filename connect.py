import pymongo
from pymongo.errors import ConnectionFailure

print('write ip')
ip = str(input())
print('write port')
port = int(input())

connect = pymongo.MongoClient(ip, port, serverSelectionTimeoutMS=3000)
try:
    connect.admin.command('ismaster')
except ConnectionFailure:
    print("not connect")
    quit()

print(connect.serverStatus) #статистика по серверу
listBd = connect.list_database_names() #список базы данных
print(listBd)
for local in listBd:
    db = connect[local]
    print(db.command("dbstats")) #cтатистика по базам банных
    listCollection = db.list_collection_names()
    print(listCollection)
    for table in listCollection:
        print(table)
        print(list(db.get_collection(table).find().limit(10)))
