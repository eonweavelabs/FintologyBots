# Utils/database_conn.py

from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)

# Provide the name of the default database
mongo_conn = "mongodb+srv://root:vGjXFpOcfKjxVFDs@fintologycluster.ltptz.mongodb.net/defaultDB?retryWrites=true&w=majority&appName=FintologyCluster"

try:
    client = MongoClient(mongo_conn, serverSelectionTimeoutMS=5000)
    myDatabase = client.get_database("defaultDB")  # Explicitly specify the database
    applications = myDatabase["applications"]
    logger.info("Successfully connected to MongoDB Atlas.")
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {e}")
    raise RuntimeError("Failed to connect to MongoDB.")
