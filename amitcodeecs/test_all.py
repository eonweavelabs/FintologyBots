# test_all.py

import pytest
from Utils.check_username_validity import validate_username
from Utils.encrypt_user_fields import encrypt_user_fields
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient
from Utils.database_conn import applications
from bson import ObjectId
import base64

# Fixture to seed MongoDB for testing
@pytest.fixture(scope="module")
def seed_mongo():
    # Insert mock data into applications collection
    seed_data = {
        "_id": ObjectId("672c131728182d825e042763"),
        "name": "Test Application",
        "client_id": ObjectId("6748a659e98239bac81c1395"),
        "personal": "test",
        "status": "new"
    }
    applications.insert_one(seed_data)
    yield
    applications.delete_one({"_id": ObjectId("672c131728182d825e042763")})

def test_validate_username():
    # White hat testing: Expected valid usernames
    valid_usernames = ["valid_user", "User123", "username_15", "A_b1"]
    for username in valid_usernames:
        assert validate_username(username), f"Username validation failed for valid username '{username}'"

    # Black hat testing: SQL injection-like inputs, starting with non-letter characters, too short, etc.
    invalid_usernames = [
        "invalid user", "123", "a", "toolongusername123456789", "_startwithunderscore",
        "DROP TABLE users;", "--comment", "Robert'); DROP TABLE Students;--"
    ]
    for username in invalid_usernames:
        assert not validate_username(username), f"Username validation passed for invalid username '{username}'"

def test_mongo_connection_fail():
    # Black box test to simulate a failed MongoDB connection
    incorrect_uri = "mongodb://invalid_user:invalid_pass@192.0.2.0:27017"  # Use a non-routable IP address
    try:
        client = MongoClient(incorrect_uri, serverSelectionTimeoutMS=2000)
        client.server_info()  # Should raise ConnectionFailure
        pytest.fail("Connection should have failed, but it succeeded.")
    except ConnectionFailure:
        assert True  # Expected outcome

def test_encrypt_user_fields(seed_mongo):
    # White box test to ensure encryption works properly
    user = applications.find_one({"_id": ObjectId("672c131728182d825e042763")})
    assert user, "User with specified ObjectId not found."

    # Encrypt fields
    encrypt_user_fields()

    # Fetch the user again and verify encryption
    encrypted_user = applications.find_one({"_id": ObjectId("672c131728182d825e042763")})
    assert encrypted_user is not None, "User with specified ObjectId not found after encryption."
    assert encrypted_user["personal"] != "test", "Encryption for personal field failed."

def test_invalid_encryption():
    # Test encryption with invalid key and IV lengths to check if errors are raised properly
    from Utils.constants import prod_encryption_key, prod_encryption_iv
    from Utils.encrypt_user_fields import encrypt_user_fields
    import Utils.encrypt_user_fields as encrypt_module

    original_key = encrypt_module.prod_encryption_key
    original_iv = encrypt_module.prod_encryption_iv

    # Set invalid key and IV
    encrypt_module.prod_encryption_key = "invalid_key"
    encrypt_module.prod_encryption_iv = "invalid_iv"

    try:
        with pytest.raises((ValueError, base64.binascii.Error), match="Invalid encryption key length|Incorrect padding"):
            encrypt_user_fields()
    finally:
        # Reset original values
        encrypt_module.prod_encryption_key = original_key
        encrypt_module.prod_encryption_iv = original_iv
