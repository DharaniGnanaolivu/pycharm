import sqlite3

def create_database():
    # Connect to or create a new database file
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    # Create a table called "users" with columns: id, username, and email
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

    def authenticate(username, password):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        query = f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

        user_id = cursor.fetchone()

        conn.close()

        return user_id

    if __name__ == "__main__":
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user_id = authenticate(username, password)

        if user_id:
            print("Login successful!")
        else:
            print("Login failed.")


