# Utils/encrypt_user_fields.py

import base64
from Crypto.Cipher import AES
from Utils.constants import prod_encryption_key, prod_encryption_iv
from Utils.database_conn import applications  # Proper import of applications
import logging

logger = logging.getLogger(__name__)

def encrypt_user_fields():
    try:
        key = base64.b64decode(prod_encryption_key)
        iv = base64.b64decode(prod_encryption_iv)

        # Check key and IV lengths
        if len(key) not in [16, 24, 32]:
            raise ValueError("Invalid encryption key length. Must be 16, 24, or 32 bytes.")
        if len(iv) != 16:
            raise ValueError("Invalid IV length. Must be 16 bytes.")

        cipher = AES.new(key, AES.MODE_CFB, iv)

        users = applications.find({})
        for user in users:
            plaintext = user.get('personal', '')
            if plaintext:
                encrypted = cipher.encrypt(plaintext.encode('utf-8'))
                applications.update_one(
                    {"_id": user["_id"]},
                    {"$set": {"personal": base64.b64encode(encrypted).decode('utf-8')}}
                )
    except (ValueError, base64.binascii.Error) as e:
        logger.error(f"Error encrypting user fields: {e}")
        raise e
