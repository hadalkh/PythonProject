from db_connection import get_connection

class UserRegister:
    def __init__(self, first_name, last_name, username, phone_number, gender, password, confirm_password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.gender = gender
        self.password = password
        self.confirm_password = confirm_password

    def register_user(self):
        if self.password != self.confirm_password:
            print("Passwords do not match.")
            return False

        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO register_user 
            (first_name, last_name, username, phone_number, gender, password)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            self.first_name,
            self.last_name,
            self.username,
            self.phone_number,
            self.gender,
            self.password  # Ideally hash passwords in a real app
        )

        try:
            cursor.execute(query, values)
            conn.commit()
            print("User registered successfully.")
            return True
        except Exception as e:
            print("User registration failed:", e)
            return False
        finally:
            cursor.close()
            conn.close()
