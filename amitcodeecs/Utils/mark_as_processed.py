import datetime
from Utils.database_conn import *

def mark_as_processed(user):
    newval={"$set": {'status': 'processed', 'datetime':datetime.datetime.utcnow()}}
    applications.update_one({'_id': user.get('application_id')}, newval) 
