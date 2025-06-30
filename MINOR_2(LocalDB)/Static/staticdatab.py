import sqlite3
import streamlit as st

class UserDatabase:
    def __init__(self, db_name="Users.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        # Check if table exists
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user'")
        table_exists = cur.fetchone()
        
        if not table_exists:
            cur.execute("""CREATE TABLE user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                phone_number TEXT,
                address TEXT,
                date_of_birth DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'active'
            )""")
        else:
            # Add new columns if they don't exist
            cur.execute("PRAGMA table_info(user)")
            columns = [c[1] for c in cur.fetchall()]
            
            new_columns = {
                'phone_number': 'TEXT',
                'address': 'TEXT',
                'date_of_birth': 'DATE',
                'created_at': 'TIMESTAMP',
                'updated_at': 'TIMESTAMP',
                'status': 'TEXT'
            }
            
            for col_name, col_type in new_columns.items():
                if col_name not in columns:
                    cur.execute(f"ALTER TABLE user ADD COLUMN {col_name} {col_type}")
        
        con.commit()
        con.close()

    def insert(self, name, email, password, phone_number='', address='', date_of_birth=None):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("""
            INSERT INTO user (name, email, password, phone_number, address, date_of_birth, created_at, updated_at, status)
            VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'active')
        """, (name, email, password, phone_number, address, date_of_birth))
        con.commit()
        con.close()

    def fetch(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("PRAGMA table_info(user)")
        columns = [c[1] for c in cur.fetchall()]
        
        cur.execute("SELECT * FROM user")
        data = cur.fetchall()
        con.close()
        
        # Return both data and column names
        return data, columns

    def describe(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("PRAGMA table_info(user)")
        data = cur.fetchall()
        con.close()
        return data

    def delete(self, id):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("DELETE FROM user WHERE id=?", (id,))
        con.commit()
        con.close()

    def update(self, id, name, email, password, phone_number='', address='', date_of_birth=None, status='active'):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("""
            UPDATE user 
            SET name=?, email=?, password=?, phone_number=?, address=?, date_of_birth=?, status=?
            WHERE id=?
        """, (name, email, password, phone_number, address, date_of_birth, status, id))
        con.commit()
        con.close()

    def get_user_by_id(self, id):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("SELECT * FROM user WHERE id=?", (id,))
        data = cur.fetchone()
        con.close()
        return data
