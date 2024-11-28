import json
import os

# Set the path where the JSON files are located
USER_FILES_PATH = '/workspaces/FintologyBots/amitcodeecs'  # Update with absolute path

# List of JSON files to validate
USER_FILES = ['Arash   Vanaki.json', 'Austin  Howard.json', 'Michael  Brown.json']
REQUIRED_FIELDS = ['username', 'email', 'card_type', 'age']  # Example of required fields

def validate_user_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for field in REQUIRED_FIELDS:
            if field not in data:
                print(f"[ERROR] Missing field '{field}' in {file_path}")
                return False
    print(f"[SUCCESS] {file_path} is valid.")
    return True

if __name__ == "__main__":
    all_valid = True
    for user_file in USER_FILES:
        # Construct the full path to the file
        file_path = os.path.join(USER_FILES_PATH, user_file)
        if not os.path.exists(file_path):
            print(f"[ERROR] File '{file_path}' not found.")
            continue
        valid = validate_user_file(file_path)
        all_valid = all_valid and valid

    if all_valid:
        print("[SUCCESS] All user files are valid.")
    else:
        print("[ERROR] One or more user files are invalid.")
