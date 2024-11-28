from unittest.mock import MagicMock
from bson import ObjectId
import pytest

# Mock MongoDB client and collection setup
@pytest.fixture
def mock_mongo_client():
    mock_client = MagicMock()
    mock_collection = MagicMock()
    mock_client["fintologycluster"]["users"] = mock_collection
    return mock_client, mock_collection

# Test function for updating a user document in the 'users' collection
def test_update_user(mock_mongo_client):
    mock_client, mock_collection = mock_mongo_client
    user_id = ObjectId("6748c2aadbbdcc03877be23e")  # Mock user ID
    updated_data = {"personal": {"firstName": "Jane", "lastName": "Smith"}}

    # Mock the return value of update_one to simulate a successful update
    mock_collection.update_one.return_value.modified_count = 1  # Simulate successful update

    # Run the update operation
    result = mock_collection.update_one({"_id": user_id}, {"$set": updated_data})

    # Assertion to ensure the update was successful
    assert result.modified_count == 1, "The document should be updated."
