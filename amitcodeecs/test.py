from Utils.database_queries import fetch_user_json

application_id = "672c131728182d825e042763"
user_data = fetch_user_json(application_id)

if user_data:
    print("User JSON fetched successfully:", user_data)
else:
    print("Failed to fetch user JSON.")
