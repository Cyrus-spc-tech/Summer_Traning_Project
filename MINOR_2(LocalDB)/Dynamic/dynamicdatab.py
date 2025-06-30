import sqlite3
import pandas as pd 
from colorama import Fore, Style,Back

class DatabaseManager:
    def __init__(self):
        self.databases = {}
        self.selected_db = None
        self.load_existing_databases()

    def load_existing_databases(self):
        import os
        for file in os.listdir():
            if file.endswith('.db'):
                db_name = file[:-3]  
                if db_name not in self.databases:
                    try:
                        self.databases[db_name] = sqlite3.connect(file)
                    except Exception as e:
                        print(f"Error loading database {db_name}: {str(e)}")
