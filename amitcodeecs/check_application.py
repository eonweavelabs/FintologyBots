from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://root:vGjXFpOcfKjxVFDs@fintologycluster.ltptz.mongodb.net/?retryWrites=true&w=majority")

db = client["fintologycluster"]  # Database name

# Insert a sample application document
application_id = "672c131728182d825e042763"
application_data = {
    "_id": ObjectId(application_id),  # Set the _id to match the one you're looking for
    "name": "Test Application",
    "client_id": ObjectId(),  # This will be an ObjectId for the associated client
    "status": "new"
}

# Insert the document into the 'applications' collection
result = db.applications.insert_one(application_data)
print(f"Inserted application with id: {result.inserted_id}")
