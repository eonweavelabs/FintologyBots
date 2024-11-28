import os

mongo_conn = os.getenv("MONGO_CONN", "default_connection_string")
print(f"MongoDB Connection: {mongo_conn}")
