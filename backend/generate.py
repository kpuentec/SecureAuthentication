import random
import string

def generate_password(length=12):
    if length < 8 or length > 20:
        raise ValueError("Password length must be between 8 and 20 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def generate_and_display_password():
    length = int(input("Enter password length (8-20): "))
    
    try:
        password = generate_password(length)
        print("\nGenerated Password (Write it down and memorize it!):")
        print(password)
        print("\nOnce you've saved it, you can use it to register.")
    except ValueError as e:
        print(e)
