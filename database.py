
#storing the events to db from hardcoded webhooks
from flask import Flask, request, abort
from flask import *
import json
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

from pymongo import MongoClient
cluster=MongoClient("mongodb+srv://jibina_2017:12345@cluster0.chx9w.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["catchalldomain"]
collection=db["events"]

#updating the events on the database from webhook,"d_n" implies the domain name and "status" True means delivered and False is
# bounced.

#receiving event1 and updating on the database
@app.route('/events/info@example.com/delivered', methods=['PUT'])
def webhook1():
    if request.method == 'PUT':
        for i in range(2000):
            db.events.insert_one({"d_n": "info@example.com", "status": True})

        print(request.json)
        return 'success', 200
    else:
        abort(400)


# receiving event2 and updating on the database
@app.route('/events/info@example.com/bounced', methods=['PUT'])
def webhook2():
    if request.method == 'PUT':
        for i in range(10):
            db.events.insert_one({"d_n": "info@example.com", "status": False})

        print(request.json)
        return 'success', 200
    else:
        abort(400)

# receiving event3 and updating on the database
@app.route('/events/foo@example.com/delivered', methods=['PUT'])
def webhook3():
    if request.method == 'PUT':
        for i in range(500):
            db.events.insert_one({"d_n": "foo@example.com", "status": True})

        print(request.json)
        return 'success', 200
    else:
        abort(400)


# receiving event4 and updating on the database
@app.route('/events/jibina@example.com/delivered', methods=['PUT'])
def webhook4():
    if request.method == 'PUT':
        for i in range(1100):
            db.events.insert_one({"d_n": "jibina@example.com", "status": True})

        print(request.json)
        return 'success', 200
    else:
        abort(400)

#created the index for the "domain_name" and "status" to imporove the speed of the query
index = db.events.create_index([ ("d_n", 1),("status",1) ])
db.events.delete_many({})

if __name__ == '__main__':
    app.run()



