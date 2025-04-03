from backend.db_handler import add_user, update_password, verify_user, create_db
from backend.password_manager import hash_password, check_password_strength
from backend.generate import generate_and_display_password

    
def display_password_strength(password):
    strength = check_password_strength(password)
    
    strength_dict = {1: "Weak", 2: "Weak", 3: "Okay", 4: "Good", 5: "Strong"}
    
    print(f"Password strength: {strength_dict[strength]}")
    
    if strength < 3:
        print("Password is weak. Please consider the following recommendations:")
        print("- Length should be between 8 and 20 characters.")
        print("- Include at least one lowercase letter, one uppercase letter, one digit, and one special character (@, $, !, %, *, ?, &, etc.).")
    
    return strength

def register():
    username = input("Enter username (max 10 characters): ")
    if len(username) > 10:
        print("Username cannot exceed 10 characters.")
        return
    
    while True:
        password = input("Enter password: ")
        if len(password) > 20:
            print("Password cannot exceed 20 characters. Please try again.")
            continue
        
        strength = display_password_strength(password)
        strength_dict = {1: "Weak", 2: "Weak", 3: "Okay", 4: "Good", 5: "Strong"}
        if strength >= 3:
            confirm = input(f"Password strength is {strength_dict[strength]}. Do you want to proceed with this password? (y/n): ")
            if confirm.lower() == 'y':
                hashed_password = hash_password(password)
                add_user(username, hashed_password)
                print("User registered successfully!")
                break
            else:
                print("Try again with a new password.")
        else:
            print("Password is too weak. Please choose a stronger one.")
    
def change_password(username):
    while True:
        
        current_password = input("Enter your current password to continue: ")
        if not verify_user(username, current_password):
            print("Current password is incorrect. Please try again.")
            continue

        new_password = input("Enter new password: ")
        if len(new_password) > 20:
            print("Password cannot exceed 20 characters. Please try again.")
            continue

        if new_password == current_password:
            print("New password cannot be the same as the old one.")
            continue
        
        strength = display_password_strength(new_password)
        if strength >= 3:
            confirm = input(f"Password strength is {strength}. Do you want to proceed with this password? (y/n): ")
            if confirm.lower() == 'y':
                hashed_new_password = hash_password(new_password)
                update_password(username, hashed_new_password)
                print("Password changed successfully!")
                break
            else:
                print("Try again with a new password.")
        else:
            print("Password is too weak. Please choose a stronger one.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if verify_user(username, password):
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

def menu():
    print("1. Register")
    print("2. Login")
    print("3. Change Password")
    print("4. Secure Password Generator")
    print("5. Exit")

def main():
    logged_in_user = None
    
    while True:
        menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            logged_in_user = login()
        elif choice == "3":
            if logged_in_user:
                change_password(logged_in_user)
            else:
                print("You must be logged in to change your password.")
        elif choice == "4":
            generate_and_display_password()
            break
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    create_db()
    main()
