import logging
from Utils.decrypt import encrypt

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_encryption():
    original_data = {
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com"
    }
    
    encrypted_data = encrypt(str(original_data))
    assert encrypted_data is not None, "Encryption failed"
    logger.info(f"Encrypted data: {encrypted_data}")
