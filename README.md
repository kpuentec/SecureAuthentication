# Secure Authentication

SecureAuthentication is a Python-based authentication system designed to securely manage user registration, login, and password updates. It enforces password strength policies, stores credentials using hashed passwords with bcrypt, and includes a built-in secure password generator. Data is stored locally in a SQLite database.

Features:

* User Registration with password strength evaluation

* Secure Login using bcrypt to hash and verify credential

* Password Change Functionality for authenticated users

* Password Strength Checker with detailed feedback

* SQLite Database for lightweight local storage

* Modular Backend separated into functional components 

Requirements:

Install Python3 onto your system(If you don't have it already).

Install:

1. Clone repository:

         git clone https://github.com/kpuentec/SecureAuthentication.git

2. Navigate to the project directory: cd PasswordValidator

3. Install requirements:

         pip install -r requirements.txt

Run:

Navigate to the root folder, cd SecureAuthentication.

Run Program

         python main.py

Structure:

* backend/ : Contains Python functions for the program

    * db_handler.py: Handles database setup, user verification, and password updates
    * password_manager.py: Manages password hashing and strength validation
    * generate.py: Generates secure passwords.

* config.py: Configuration file for database path

* main.py: Main script handling user interaction and authentication flow

* .gitignore : Git ignore file to exclude unnecessary files

* LICENSE : Project license info

*README.md: This file

Output:

* database.db: SQLite database storing user credentials (generated on first run)

**Notes:** 

* Passwords are hashed using bcrypt and never stored in plain text.

* Username is limited to 10 characters; passwords are between 8–20 characters.

* Passwords must include lowercase, uppercase, digits, and special characters to be considered strong.

* Project is modular and easy to expand

* Changes to the code and other features are susceptible in the future

2025

