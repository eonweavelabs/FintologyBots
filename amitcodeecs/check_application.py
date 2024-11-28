from pymongo import MongoClient
from bson.objectid import ObjectId

# Connection URI
uri = "mongodb+srv://root:vGjXFpOcfKjxVFDs@fintologycluster.ltptz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["fintologycluster"]

# Document to insert
application_data = {
    "_id": ObjectId("672c131728182d825e042763"),
    "client_id": ObjectId("some_client_id"),  # Replace with a valid client_id from your users collection
    # Add any other fields required by your logic
}

# Insert document
db.applications.insert_one(application_data)
print(f"Inserted application with id: {application_data['_id']}")
