import mailslurp_client
from random import randint
from Utils.constants import *
from Utils.database_conn import *
import datetime
from bson.objectid import ObjectId
from Utils.check_username_validity import check_username_validity
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = MAILSLURP_API_KEY




def create_inbox(user):
    client_id=user.get("client_id")
    if(type(client_id)==str):
        client_id=ObjectId(client_id)
    name=user.get("personal").get("firstName", "")+user.get("personal").get("lastName", "")
    if(len(name)>13):
        if(user.get("personal").get("lastName", "")!=None):
            name=user.get("personal").get("lastName", "")[0]+user.get("personal").get("firstName", "")
        else:
            name=user.get("personal").get("lastName", "")
    name=name.replace(" ", "")
    name=name.lower()
    custom_email=f'{name}_{randint(10, 100)}@{MAILSLURP_DOMAIN}'
    if(check_username_validity(custom_email)):
        with mailslurp_client.ApiClient(configuration) as api_client:
            api_instance = mailslurp_client.InboxControllerApi(api_client)
            inbox = api_instance.create_inbox(inbox_type="SMTP_INBOX", email_address=custom_email)
            temp=clients.find_one({"_id": client_id})
            temp.update({"mailing":{'email': inbox.email_address, 'id':inbox.id, 'datetime':datetime.datetime.utcnow()}})
            newval={"$set": temp}
            clients.update_one({'_id': client_id}, newval, upsert=False)
            return inbox.email_address
        
        

