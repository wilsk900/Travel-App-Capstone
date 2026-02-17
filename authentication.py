import pandas as pd
import bcrypt
import os

FILE_NAME = "users.xlsx"

# Creates file if it doesn't exist
def initialize_database():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["username", "password"])
        df.to_excel(FILE_NAME, index=False)

# Loads users
def load_users():
    return pd.read_excel(FILE_NAME)

# Saves users
def save_users(df):
    df.to_excel(FILE_NAME, index=False)

# Registers users
def register_user(username, password):
    df = load_users()

    if username in df["username"].values:
        return False

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    new_user = pd.DataFrame({
        "username": [username],
        "password": [hashed.decode()]
    })

    df = pd.concat([df, new_user], ignore_index=True)
    save_users(df)

    return True

# Verify login
def login_user(username, password):
    df = load_users()

    if username not in df["username"].values:
        return False

    stored_password = df[df["username"] == username]["password"].values[0]

    return bcrypt.checkpw(password.encode(), stored_password.encode())




