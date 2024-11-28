# File: Utils/decrypt.py

import logging
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the actual encryption key and IV as string variables
prod_encryption_key = "1+RO/h1lU55DOnbuJHC3yku8lfTYxlc+f71IawGyMpk="  # Replace this with your actual key
prod_encryption_iv = "MxsPyuNmQCr6ZhD85ao7bg=="  # Replace this with your actual IV

# Function to fix Base64 padding
def fix_base64_padding(data):
    """Fixes Base64 padding by adding the necessary '=' characters"""
    missing_padding = len(data) % 4
    if missing_padding:
        data += '=' * (4 - missing_padding)
    return data

# Encrypt function
def encrypt(data):
    """Encrypt data using the appropriate key and IV."""
    try:
        iv = base64.b64decode(fix_base64_padding(prod_encryption_iv))  # Fix the IV padding
        key = base64.b64decode(fix_base64_padding(prod_encryption_key))  # Fix the key padding
        
        # Create cipher config and perform encryption
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(data.encode("utf-8"), AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        
        # Return the encrypted data in base64 format
        return base64.b64encode(encrypted_data).decode('utf-8')

    except Exception as e:
        logger.error(f"Error during encryption: {e}")
        return None
