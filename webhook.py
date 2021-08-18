
#creating webhooks as hard coded events
import requests
import json
import main


from pymongo import MongoClient
cluster=MongoClient("mongodb+srv://jibina_2017:12345@cluster0.chx9w.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["catchalldomain"]
collection=db["events"]




#sending event1 through webhook
url1 = "http://127.0.0.1:5000/events/info@example.com/delivered"
data = {"d_n": "info@example.com", "status": True}

r1 = requests.put(url1, data=json.dumps(data), headers={'Content-Type': 'application/json'})
#sending event2 through webhook
url2 = "http://127.0.0.1:5000/events/info@example.com/bounced"
data = {"d_n": "info@example.com", "status": False}

r2 = requests.put(url2, data=json.dumps(data), headers={'Content-Type': 'application/json'})

#sending event3 through webhook
url3 = "http://127.0.0.1:5000/events/foo@example.com/delivered"
data = {"d_n": "foo@example.com", "status": True}

r3 = requests.put(url3, data=json.dumps(data), headers={'Content-Type': 'application/json'})

#sending event4 through webhook
url4 = "http://127.0.0.1:5000/events/jibina@example.com/delivered"
data = {"d_n": "jibina@example.com", "status": True}

r4 = requests.put(url4, data=json.dumps(data), headers={'Content-Type': 'application/json'})