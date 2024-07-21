import tkinter as tk
from tkinter import simpledialog
import json
import os

def add_user(root, users, user_dropdown):
    print("Prompting user for name...")
    user_name = simpledialog.askstring("Add User", "Enter user name:", parent=root)
    
    if user_name:
        print(f"User name entered: {user_name}")
        
        users.append(user_name)
        print(f"Updated users list: {users}")
        
        user_dropdown['values'] = users
        print("Updated user_dropdown values.")
        
        save_users(users)
        print("Users saved to file.")
    else:
        print("No user name entered.")

def save_users(users):
    users_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'files', 'users.json'))
    
    print(f"Saving users to file: {users_file_path}")
    
    with open(users_file_path, 'w') as file:
        json.dump(users, file)
    
    print("Users saved successfully.")

def load_users():
    users_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'files', 'users.json'))
    
    if os.path.exists(users_file_path):
        print(f"Loading users from file: {users_file_path}")
        with open(users_file_path, 'r') as file:
            users = json.load(file)
        print("Users loaded successfully.")
        return users
    else:
        print("Users file does not exist.")
        return []
