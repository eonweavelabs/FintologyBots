from pymongo import MongoClient
from Utils.constants import mongo_conn
client = MongoClient(mongo_conn)
myDatabase = client['production']

users=myDatabase['onboarding']
old_users=myDatabase['old_onboarding']
applications=myDatabase['applications']
products=myDatabase['products']
clients=myDatabase['clients']
old_clients=myDatabase['old_clients']
businessOnboarding=myDatabase['business_onboarding']
domains=myDatabase['domains']