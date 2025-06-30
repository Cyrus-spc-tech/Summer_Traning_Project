import sqlite3

class DatabaseHelper:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE Table IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_user(self, name, age):
        self.cursor.execute('''
            INSERT INTO users (name, age) VALUES (?, ?)
        ''', (name, age))
        self.connection.commit()

    def fetch_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def describe_table(self):
        self.cursor.execute('PRAGMA table_info(users)')
        return self.cursor.fetchall()

    def update_user(self, user_id, name, age):
        self.cursor.execute('''
            UPDATE users SET name = ?, age = ? WHERE id = ?
        ''', (name, age, user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute('''
            DELETE FROM users WHERE id = ?
        ''', (user_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()
