
#performing the logic to find domain_name is "catch all","not catch all" and "unknown"
from flask import Flask, redirect, url_for, request,abort
import pymongo
import os
import requests
from pymongo import MongoClient
cluster=MongoClient("mongodb+srv://jibina_2017:12345@cluster0.chx9w.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["catchalldomain"]
collection=db["events"]



app = Flask(__name__)

#fetching the domain_name from the db and checking the status
@app.route('/events/<name>')
def query(name):
   delivered=(db.events.count_documents({'d_n':name,"status":True}))
   bounced=(db.events.count_documents({'d_n':name,"status":False}))

   if bounced > 0:
      print("not catch all domain")
      print("Number of bounced emails are",bounced)
      return str(name) +     " = not catch all"
   elif delivered <1000:
      print("unknown")
      print("Number of delivered emails are", delivered)
      return str(name) +   "= unknown"


   elif delivered >1000:
      print("catch all domain")
      print("Number of delivered emails are", delivered)
   return   str(name) +    "= catch all"




#getting the domain_name from customer query and redirecting to the function to fetch the count from db
@app.route('/events/domain',methods = ['PUT', 'GET'])
def domain():
   if request.method == 'PUT':
      user = request.form['nm']
      return redirect(url_for('query',name = user,))
   else:
      user = request.args.get('nm')

      return redirect(url_for('query',name = user))




if __name__ == '__main__':
   app.run(debug = True)






