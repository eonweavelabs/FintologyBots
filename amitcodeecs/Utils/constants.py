# Utils/constants.py

import base64

mongo_conn = "mongodb+srv://root:vGjXFpOcfKjxVFDs@fintologycluster.ltptz.mongodb.net/?retryWrites=true&w=majority&appName=FintologyCluster"

MAILSLURP_API_KEY = "8eb48b02bc8c61ba6c2d60f8f26506add361ae9fb792cc13739cf3b294436773"
MAILSLURP_DOMAIN = "member.fintology.ai"
WEBSHARE_API_KEY = "8vvmwp34tgvzze9oti3wgo6eq8nc89g53c0rc6ks"

# Updated encryption key and IV to be of correct length
prod_encryption_key = base64.b64encode(b'0123456789ABCDEF0123456789ABCDEF').decode('utf-8')  # 32 bytes
prod_encryption_iv = base64.b64encode(b'0123456789ABCDEF').decode('utf-8')  # 16 bytes

DEV_MACHINE_NAME = ["localhost", "127.0.0.1"]

proxylist = [
    "154.194.16.140:6059",
    "72.46.139.16:6576",
    # Add the rest of your proxy list here
]

business_card_list = [
    "Chase Ink Business Cash",
    "US Bank Triple Cash Rewards Visa Card",
    # Add more business cards as needed
]

personal_card_list = [
    "Discover it Cash Back",
    "Capital One Quick Silver",
    # Add more personal cards as needed
]
