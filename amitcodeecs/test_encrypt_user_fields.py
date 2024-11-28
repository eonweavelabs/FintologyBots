from unittest.mock import patch, MagicMock
from Utils.encrypt_user_fields import encrypt_user_fields  # Assuming this is the correct path

def test_encrypt_user_fields():
    mock_mongo_client = MagicMock()
    mock_collection = MagicMock()
    mock_user = {
        "_id": "6748c2aadbbdcc03877be23e",
        "personal": {"firstName": "John", "lastName": "Doe"},
        "preApproval": {"fundingType": "personal"},
        "business": {"businessName": "Doe Enterprises"}
    }
    
    # Mock the return value of the find_one call to return a user
    mock_collection.find_one.return_value = mock_user
    mock_collection.update_one.return_value.modified_count = 1
    
    with patch('Utils.encrypt_user_fields.users_collection', mock_collection), \
         patch('Utils.decrypt.encrypt') as mock_encrypt:
    
        # Mock the encryption function to return a mock encrypted string
        mock_encrypt.return_value = "encrypted_data"
    
        # Run the function
        encrypt_user_fields()
    
        # Check that update_one was called with fields that are not empty
        update_call_args = mock_collection.update_one.call_args[0][1]  # Get the second argument of the first call
        
        # Assert that 'personal', 'preApproval', and 'business' are present in the $set dictionary and are not empty
        assert 'personal' in update_call_args['$set']
        assert update_call_args['$set']['personal'] != ""
        assert 'preApproval' in update_call_args['$set']
        assert update_call_args['$set']['preApproval'] != ""
        assert 'business' in update_call_args['$set']
        assert update_call_args['$set']['business'] != ""
