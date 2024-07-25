from userdb import *
from dborm import *

if __name__ == "__main__":
    db = UserDatabase(host="127.0.0.1", user="root", password = "", database = "hanabank", port = 3306)
    
    # Create a new user
    db.create_user('강하리', 27)
    
    # Read users
    users = db.read_users()
    for user in users:
        print(user)
    
    # Update a user
    db.update_user(user_id=3, new_name='세종대왕', new_age=30)
    
    # Delete a user
    db.delete_user(user_id=3)