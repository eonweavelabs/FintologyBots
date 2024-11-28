# File: Utils/encrypt_user_fields.py

import logging
from .decrypt import encrypt  # Relative import for encrypt
from .constants import *      # Relative import for constants

from pymongo import MongoClient
from bson.objectid import ObjectId

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB connection setup
client = MongoClient(mongo_conn)  # mongo_conn should be your MongoDB connection string
db = client["fintologycluster"]
users_collection = db["users"]

def encrypt_user_fields():
    """Encrypts specific user fields in the MongoDB collection"""
    try:
        user = users_collection.find_one()  # Fetches the first document from the collection

        if not user:  # If no user is found, exit the function
            logger.info("No user documents found in the collection.")
            return

        update_fields = {}  # This will hold the encrypted fields

        # Encrypting the 'personal' field
        if "personal" in user:
            encrypted_personal = encrypt(str(user["personal"]))  # Encrypt the personal field
            update_fields["personal"] = encrypted_personal
            logger.info(f"Encrypted 'personal' field for user: {user['_id']}")

        # Encrypting the 'preApproval' field
        if "preApproval" in user:
            encrypted_preApproval = encrypt(str(user["preApproval"]))  # Encrypt preApproval field
            update_fields["preApproval"] = encrypted_preApproval
            logger.info(f"Encrypted 'preApproval' field for user: {user['_id']}")

        # Encrypting the 'business' field
        if "business" in user:
            encrypted_business = encrypt(str(user["business"]))  # Encrypt business field
            update_fields["business"] = encrypted_business
            logger.info(f"Encrypted 'business' field for user: {user['_id']}")

        # Update the MongoDB document with the encrypted fields
        if update_fields:  # If there are fields to update, update the document
            logger.info(f"Attempting to update user: {user['_id']} with encrypted fields: {update_fields}")
            users_collection.update_one({"_id": user["_id"]}, {"$set": update_fields})
            logger.info(f"Updated user: {user['_id']} with encrypted fields.")
        else:
            logger.info(f"No fields to encrypt for user: {user['_id']}")

    except Exception as e:
        logger.error(f"Error encrypting user fields: {e}")
