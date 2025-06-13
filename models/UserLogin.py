from db_connection import get_connection

class UserLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM register_user WHERE username = %s AND password = %s"
        cursor.execute(query, (self.username, self.password))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            return True
        else:
            return False