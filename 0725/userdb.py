import datetime
import pymysql

class UserDatabase:
    def __init__(self, host, user, password, database, port):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port = port
        )
        self.cursor = self.connection.cursor()
        print("Database connection established.")

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")
    
    def create_user(self, name, age):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO USER (NAME, AGE, _CREATED_AT, _UPDATED_AT) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (name, age, now, now))
        self.connection.commit()
        print("User created.")
        print(f"Last executed query: {query % (name, age, now, now)}")
    
    def read_users(self):
        query = "SELECT * FROM user"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        print("Users retrieved.")
        print(f"Last executed query: {query}")
        return results
    
    def update_user(self, user_id, new_name, new_age=None):
        update_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "UPDATE user SET NAME = %s, _UPDATED_AT = %s"
        params = [new_name, update_now]
        if new_age is not None:
            query += ", AGE = %s"
            params.append(new_age)
        query += " WHERE ID = %s"
        params.append(user_id)
        self.cursor.execute(query, tuple(params))
        self.connection.commit()
        print("User updated.")
        print(f"Last executed query: {query % tuple(params)}")
    
    def delete_user(self, user_id):
        query = "DELETE FROM user WHERE ID = %s"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        print("User deleted.")
        print(f"Last executed query: {query % user_id}")