from pymongo import MongoClient
from Utils.constants import mongo_conn
import logging

# Initialize logger
logger = logging.getLogger(__name__)

try:
    # Establish MongoDB connection
    client = MongoClient(mongo_conn)
    logger.info("Successfully connected to MongoDB.")
except Exception as e:
    logger.error(f"Failed to connect to MongoDB: {e}")
    raise

try:
    # Specify the database
    myDatabase = client['fintologycluster']  # Confirm this matches your actual database name
    logger.info(f"Connected to database: fintologycluster")

    # Define collections
    users = myDatabase['users']
    old_users = myDatabase['old_users']  # Verify this collection exists or adjust the name
    applications = myDatabase['applications']
    products = myDatabase['products']
    clients = myDatabase['clients']
    old_clients = myDatabase['old_clients']  # Confirm this collection name is accurate
    businessOnboarding = myDatabase['business_onboarding']
    domains = myDatabase['domains']

    # Log collection list for confirmation
    logger.info(f"Collections in the database: {myDatabase.list_collection_names()}")

except Exception as e:
    logger.error(f"Error accessing database or collections: {e}")
    raise
