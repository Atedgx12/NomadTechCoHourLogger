import os

def get_current_user():
    try:
        user = os.getlogin()
        print(f"Current user retrieved: {user}")
        return user
    except Exception as e:
        print(f"Error retrieving current user: {e}")
        raise
