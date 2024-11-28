import os
import base64

# Generate 32-byte encryption key for AES-256
key = os.urandom(32)  # 32 bytes = 256 bits
# Generate 16-byte initialization vector (IV)
iv = os.urandom(16)  # 16 bytes = 128 bits

# Base64 encode the key and IV to make them suitable for storage or use in your app
prod_encryption_key = base64.b64encode(key).decode('utf-8')
prod_encryption_iv = base64.b64encode(iv).decode('utf-8')

# Print the key and IV
print("Encryption Key:", prod_encryption_key)
print("Encryption IV:", prod_encryption_iv)
