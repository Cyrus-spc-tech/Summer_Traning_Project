import sqlite3
import pandas as pd 
from colorama import Fore, Style,Back

class DatabaseManager:
    def __init__(self):
        self.databases = {}
        self.selected_db = None
        
    def create_database(self, db_name):
        """Create a new database"""
        if db_name in self.databases:
            return False, "Database already exists"
            
        self.databases[db_name] = sqlite3.connect(f"{db_name}.db")
        return True, "Database created successfully"
        
    def select_database(self, db_name):
        """Select an existing database"""
        if db_name not in self.databases:
            return False, "Database does not exist"
            
        self.selected_db = self.databases[db_name]
        return True, "Database selected successfully"
        
    def create_table(self, table_name, columns):
        """Create a new table with custom columns"""
        if not self.selected_db:
            return False, "No database selected"
            
        # Validate column definitions
        if not isinstance(columns, dict):
            return False, "Columns must be a dictionary"
            
        # Build SQL query
        columns_sql = []
        for col_name, col_type in columns.items():
            # Add basic validation for column types
            if col_type not in ['TEXT', 'INTEGER', 'REAL', 'DATE', 'TIMESTAMP']:
                return False, f"Invalid column type: {col_type}"
            columns_sql.append(f"{col_name} {col_type}")
            
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns_sql)})"
        
        try:
            self.selected_db.execute(sql)
            self.selected_db.commit()
            return True, "Table created successfully"
        except sqlite3.Error as e:
            return False, str(e)
            
    def get_tables(self):
        """Get list of tables in the selected database"""
        if not self.selected_db:
            return [], "No database selected"
            
        cursor = self.selected_db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [row[0] for row in cursor.fetchall()], ""
        
    def get_columns(self, table_name):
        """Get columns of a specific table"""
        if not self.selected_db:
            return [], "No database selected"
            
        cursor = self.selected_db.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        return cursor.fetchall(), ""
        
    def insert_data(self, table_name, data):
        """Insert data into a table"""
        if not self.selected_db:
            return False, "No database selected"
            
        cursor = self.selected_db.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [col[1] for col in cursor.fetchall()]
        
        # Validate data
        if not all(key in columns for key in data.keys()):
            return False, "Invalid column names in data"
            
        placeholders = ', '.join(['?'] * len(data))
        columns_str = ', '.join(data.keys())
        values = tuple(data.values())
        
        sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
        
        try:
            cursor.execute(sql, values)
            self.selected_db.commit()
            return True, "Data inserted successfully"
        except sqlite3.Error as e:
            return False, str(e)
            
    def fetch_data(self, table_name, query=None):
        """Fetch data from a table with optional query"""
        if not self.selected_db:
            return None, "No database selected"
            
        cursor = self.selected_db.cursor()
        if query:
            cursor.execute(query)
        else:
            cursor.execute(f"SELECT * FROM {table_name}")
            
        rows = cursor.fetchall()
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [col[1] for col in cursor.fetchall()]
        
        return pd.DataFrame(rows, columns=columns), ""
        
    def delete_table(self, table_name):
        """Delete a table"""
        if not self.selected_db:
            return False, "No database selected"
            
        try:
            self.selected_db.execute(f"DROP TABLE IF EXISTS {table_name}")
            self.selected_db.commit()
            return True, "Table deleted successfully"
        except sqlite3.Error as e:
            return False, str(e)
            
    def delete_database(self, db_name):
        """Delete a database"""
        if db_name not in self.databases:
            return False, "Database does not exist"
            
        try:
            self.databases[db_name].close()
            del self.databases[db_name]
            return True, "Database deleted successfully"
        except Exception as e:
            return False, str(e)