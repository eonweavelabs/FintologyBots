# Utils/check_username_validity.py

import re

def validate_username(username: str) -> bool:
    # Regex pattern to match a username that starts with a letter and can have letters, numbers, and underscores
    # Length between 3 and 20 characters.
    pattern = re.compile(r"^[A-Za-z][A-Za-z0-9_]{2,19}$")
    
    # Additional check for SQL injection-like inputs and unsafe characters
    if ";" in username or "--" in username or "'" in username or "DROP" in username.upper():
        return False  # Prevent SQL injection and unsafe characters.

    return bool(pattern.match(username))
