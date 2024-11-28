from Utils.database_conn import *
from bson.objectid import ObjectId
from Utils.convert_str import convert_str
import json
import datetime
from Utils.decrypt import decrypt
import logging

logger = logging.getLogger(__name__)

def check_email_exists(user):
    client_id = user.get("client_id")
    if not isinstance(client_id, ObjectId):
        client_id = ObjectId(client_id)

    mailing = clients.find_one({"_id": client_id})
    if mailing:
        try:
            if mailing.get("mailing").get("id"):
                return True, mailing.get("mailing").get("email")
        except AttributeError:
            return False, None
    return False, None

def fetch_user_json(application_id, write_to_json=False):
    try:
        # Find the application by ID
        application = applications.find_one({"_id": ObjectId(application_id)})
        if application is None:
            logger.error(f"Application with id {application_id} not found.")
            return None

        # Extract client_id from the application
        client_id = application.get("client_id")
        if client_id is None:
            logger.error(f"No client_id found for application_id {application_id}.")
            return None

        # Find user details by client_id
        tempuser = users.find_one({'client_id': client_id})
        if tempuser is None:
            logger.error(f"No user found with client_id {client_id}.")
            return None

        # Retrieve and decrypt user data
        business = convert_str(json.loads(decrypt(tempuser.get("business", "{}")))) if tempuser.get("business") else {}
        personal = convert_str(json.loads(decrypt(tempuser.get("personal", "{}")))) if tempuser.get("personal") else {}
        preApproval = convert_str(json.loads(decrypt(tempuser.get("preApproval", "{}")))) if tempuser.get("preApproval") else {}

        # Determine the application type
        ApplicationType = "business" if business else "personal"

        # Create a dictionary to hold user information
        tempdict = {
            "client_id": str(client_id) if write_to_json else client_id,
            "application_id": str(application_id),
            "email": clients.find_one({"_id": client_id}).get('mailing', {}).get('email', 'unknown@example.com'),
            "preApproval": preApproval,
            "business": business,
            "personal": personal,
        }

        return tempdict

    except Exception as e:
        logger.error(f"Error fetching user JSON for application_id {application_id}: {e}", exc_info=True)
        return None

def mark_as_processed(user):
    newval = {"$set": {'status': 'processed', 'datetime': datetime.datetime.utcnow()}}
    applications.update_one({'_id': ObjectId(user.get('application_id'))}, newval)
