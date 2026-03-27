import hashlib
from utils import load_data, save_data


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    data = load_data()

    username = input("Enter username: ").strip()
    if username in data["users"]:
        print("❌ Username already exists")
        return

    password = input("Enter password: ").strip()
    if len(password) < 4:
        print("❌ Password too short")
        return

    data["users"][username] = {
        "password": hash_password(password),
        "loans": []
    }

    save_data(data)
    print("✅ Registration successful")


def login():
    data = load_data()

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username not in data["users"]:
        print("❌ User not found")
        return None

    if data["users"][username]["password"] == hash_password(password):
        print(f"✅ Welcome {username}")
        return username
    else:
        print("❌ Wrong password")
        return None
