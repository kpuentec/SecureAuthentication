import bcrypt
import re

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def check_password(stored_hash, password):
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)

def check_password_strength(password):
    if len(password) < 8 or len(password) > 20:
        return 1
    
    has_lower = re.search(r'[a-z]', password) is not None
    has_upper = re.search(r'[A-Z]', password) is not None
    has_digit = re.search(r'[0-9]', password) is not None
    has_special = re.search(r'[@$!%*?&^#()_\-+=|<>]', password) is not None

    strength = 1
    if has_lower:
        strength += 1
    if has_upper:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    
    return strength