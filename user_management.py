import json
from datetime import datetime

USER_FILE = "data/users.json"

# read_file; Utility function to safely handle file operations
# load_users; Load user data from the JSON file
# save_users; Save user data back to the JSON file
# get_user; Retrieve an existing user or return None
# create_user; Create a new user profile
# update_user_history; Update a user's quiz history with a new score

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_file(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_users():
    return read_file(USER_FILE)


def save_users(users):
    write_file(USER_FILE, users)


def get_user(username):
    return next((user for user in load_users() if user["name"] == username), None)


def create_user(username):
    if get_user(username):
        raise ValueError(f"User '{username}' already exists.")
    new_user = {"name": username, "history": []}
    users = load_users()
    users.append(new_user)
    save_users(users)
    return new_user

def update_user_history(username, score):
    users = load_users()
    user = next((u for u in users if u["name"] == username), None)
    if not user:
        raise ValueError(f"User '{username}' not found.")
    user["history"].append({"date": datetime.now().isoformat(), "score": score})
    save_users(users)
