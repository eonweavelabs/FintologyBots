from Utils.database_conn import myDatabase, users

try:
    print(f"Collections: {myDatabase.list_collection_names()}")
    sample_user = users.find_one()
    print(f"Sample user document: {sample_user}")
except Exception as e:
    print(f"Test failed: {e}")
