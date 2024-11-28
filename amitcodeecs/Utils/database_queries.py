from Utils.database_conn import *  # MongoDB connection is assumed to be here
from bson.objectid import ObjectId
from Utils.convert_str import convert_str
import json
import datetime
from Utils.decrypt import decrypt
import logging

logger = logging.getLogger(__name__)

def check_email_exists(user):
    """
    Check if an email exists for the given user in the clients collection.
    """
    client_id = user.get("client_id")
    if not isinstance(client_id, ObjectId):
        client_id = ObjectId(client_id)

    try:
        mailing = clients.find_one({"_id": client_id})
        if mailing:
            try:
                if mailing.get("mailing", {}).get("id"):
                    return True, mailing.get("mailing").get("email")
            except AttributeError:
                return False, None
        return False, None
    except Exception as e:
        logger.error(f"Error checking email for user with client_id {client_id}: {e}")
        return False, None


def fetch_user_json(application_id, write_to_json=False):
    try:
        # Fetch application document
        application = applications.find_one({"_id": ObjectId(application_id)})
        if not application:
            raise ValueError(f"Application with id {application_id} not found.")
        print(f"Application Found: {application}")

        # Extract and validate client_id
        client_id = application.get("client_id")
        if not client_id:
            raise ValueError(f"Client ID for application {application_id} not found.")
        print(f"Client ID Found: {client_id}")
        if not isinstance(client_id, ObjectId):
            client_id = ObjectId(client_id)

        # Fetch user document
        user = users.find_one({"client_id": client_id})
        if not user:
            raise ValueError(f"No user document found for client_id: {client_id}.")
        print(f"User Document Found: {user}")

        # Validate fields
        if not isinstance(user.get("preApproval"), str):
            raise ValueError(f"Field preApproval is not properly encrypted in the user document.")
        if user.get("business") and not isinstance(user["business"], str):
            raise ValueError(f"Field business is not properly encrypted in the user document.")
        if not isinstance(user.get("personal"), str):
            raise ValueError(f"Field personal is not properly encrypted in the user document.")

        # Decrypt and process fields
        user_data = {
            "client_id": str(client_id),
            "application_id": str(application_id),
            "email": clients.find_one({"_id": client_id}).get("mailing", {}).get("email"),
            "preApproval": convert_str(json.loads(decrypt(user["preApproval"]))),
            "business": convert_str(json.loads(decrypt(user["business"]))) if user.get("business") else {},
            "personal": convert_str(json.loads(decrypt(user["personal"])))
        }

        return user_data

    except Exception as e:
        logger.error(f"Error fetching user JSON for application_id {application_id}: {e}")
        return None





def mark_as_processed(user):
    """
    Mark the application as processed in the database.
    """
    try:
        newval = {"$set": {'status': 'processed', 'datetime': datetime.datetime.utcnow()}}
        applications.update_one({'_id': ObjectId(user.get('application_id'))}, newval)
        logger.info(f"Marked application_id {user.get('application_id')} as processed.")
    except Exception as e:
        logger.error(f"Error marking application_id {user.get('application_id')} as processed: {e}")
