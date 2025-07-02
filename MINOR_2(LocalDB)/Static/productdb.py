import sqlite3
import streamlit as st

class ProductDatabase:
    def __init__(self, db_name="Product.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        # Check if table exists
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Product'")
        table_exists = cur.fetchone()
        
        if not table_exists:
            cur.execute("""CREATE TABLE Product(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price TEXT NOT NULL,
                quantity TEXT NOT NULL,
                stockid TEXT NOT NULL,
                description TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'active'
            )""")
        else:
            # Add new columns if they don't exist
            cur.execute("PRAGMA table_info(Product)")
            columns = [c[1] for c in cur.fetchall()]
            
            new_columns = {
                'price': 'TEXT',
                'quantity': 'TEXT',
                'stockid': 'TEXT',
                'description': 'TEXT',
                'created_at': 'TIMESTAMP',
                'updated_at': 'TIMESTAMP',
                'status': 'TEXT'
            }
            
            for col_name, col_type in new_columns.items():
                if col_name not in columns:
                    cur.execute(f"ALTER TABLE Product ADD COLUMN {col_name} {col_type}")
        
        con.commit()
        con.close()







    def insert(self, name, price, quantity, stockid, description):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("""
            INSERT INTO Product (name, price, quantity, stockid, description, created_at, updated_at, status)
            VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'active')
        """, (name, price, quantity, stockid, description))
        con.commit()
        con.close()








    def fetch(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("PRAGMA table_info(Product)")
        columns = [c[1] for c in cur.fetchall()]
        
        cur.execute("SELECT * FROM Product")
        data = cur.fetchall()
        con.close()
        
        # Return both data and column names
        return data, columns










    def describe(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("PRAGMA table_info(Product)")
        data = cur.fetchall()
        con.close()
        return data







    def delete(self, id):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("DELETE FROM Product WHERE id=?", (id,))
        con.commit()
        con.close()








    def update(self, id, name, price, quantity, stockid, description, status='active'):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("""
            UPDATE Product 
            SET name=?, price=?, quantity=?, stockid=?, description=?, status=?
            WHERE id=?
        """, (name, price, quantity, stockid, description, status, id))
        con.commit()
        con.close()





    def get_product_by_id(self, id):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("SELECT * FROM Product WHERE id=?", (id,))
        data = cur.fetchone()
        con.close()
        return data
