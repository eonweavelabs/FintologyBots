import sys
import os
import pytest

# Add the parent directory to sys.path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Utils.encrypt_user_fields import encrypt_user_fields  # Adjust according to your structure

@pytest.fixture
def mock_mongo_client():
    mock_client = MagicMock()
    mock_collection = MagicMock()
    mock_client["fintologycluster"]["users"] = mock_collection
    return mock_client, mock_collection

def test_mongo_connection(mock_mongo_client):
    mock_client, mock_collection = mock_mongo_client
    
    # Ensure that the 'users' collection is accessed from the mock database
    mock_client["fintologycluster"]["users"]
    
    # Ensure find_one was called
    mock_collection.find_one.assert_called_once()

def test_encrypt_user_fields(mock_mongo_client):
    mock_client, mock_collection = mock_mongo_client
    mock_collection.find_one.return_value = {"_id": "some_id", "personal": "test", "preApproval": "test", "business": "test"}
    mock_collection.update_one.return_value.modified_count = 1
    
    # Mock encryption function
    with patch('Utils.decrypt.encrypt') as mock_encrypt:
        mock_encrypt.return_value = "encrypted_data"
        
        # Call the function that should trigger the update
        encrypt_user_fields()

        # Ensure update_one was called with encrypted data
        mock_collection.update_one.assert_called_once_with(
            {"_id": "some_id"},
            {"$set": {"personal": "encrypted_data", "preApproval": "encrypted_data", "business": "encrypted_data"}}
        )

def test_end_to_end(mock_mongo_client):
    mock_client, mock_collection = mock_mongo_client
    mock_collection.find_one.return_value = {"_id": "some_id", "personal": "test", "preApproval": "test", "business": "test"}
    
    # Mock encryption
    with patch('Utils.decrypt.encrypt') as mock_encrypt:
        mock_encrypt.return_value = "encrypted_data"
        
        # Call the function under test
        encrypt_user_fields()
    
        # Ensure update_one was called as expected
        mock_collection.update_one.assert_called_once_with(
            {"_id": "some_id"},
            {"$set": {"personal": "encrypted_data", "preApproval": "encrypted_data", "business": "encrypted_data"}}
        )
