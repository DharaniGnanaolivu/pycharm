import sqlite3

def login_safe(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))

    user_data = cursor.fetchone()
    conn.close()

    return user_data

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    user_data = login_safe(username, password)
    if user_data:
        print("Login successful.")
    else:
        print("Login failed.")