import sqlite3
import os

class DatabaseHelper:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseHelper, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lead_management.db')
    
    def get_connection(self):
        try:
            connection = sqlite3.connect(self.db_path)
            connection.execute("PRAGMA foreign_keys = ON")
            connection.row_factory = sqlite3.Row
            return connection
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None
    
    def get_data(self, query, params=None):
        connection = self.get_connection()
        if connection is None:
            return None
        
        try:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            result = [dict(row) for row in rows]
            return result
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
    
    def get_single_data(self, query, params=None):
        connection = self.get_connection()
        if connection is None:
            return None
        
        try:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            row = cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
    
    def insert(self, query, params=None):
        connection = self.get_connection()
        if connection is None:
            return 0
        
        try:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            insert_id = cursor.lastrowid
            return insert_id
        except Exception as e:
            print(f"Error inserting data: {e}")
            connection.rollback()
            return 0
        finally:
            cursor.close()
            connection.close()
    
    def update(self, query, params=None):
        connection = self.get_connection()
        if connection is None:
            return 0
        
        try:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            affected_rows = cursor.rowcount
            return affected_rows
        except Exception as e:
            print(f"Error updating data: {e}")
            connection.rollback()
            return 0
        finally:
            cursor.close()
            connection.close()
    
    def delete(self, query, params=None):
        connection = self.get_connection()
        if connection is None:
            return 0
        
        try:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            affected_rows = cursor.rowcount
            return affected_rows
        except Exception as e:
            print(f"Error deleting data: {e}")
            connection.rollback()
            return 0
        finally:
            cursor.close()
            connection.close()

db = DatabaseHelper()

SECRET_KEY = "your-secret-key-here"
JWT_EXPIRY = 3600