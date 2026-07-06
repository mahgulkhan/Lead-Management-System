import mysql.connector
from mysql.connector import Error

class DatabaseHelper:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseHelper, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.server_name = "127.0.0.1"
        self.port = 3306
        self.database_name = "lead_management"
        self.database_user = "root"
        self.database_password = "`1234567890-=`1234567890-=" 
    
    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.server_name,
                port=self.port,
                user=self.database_user,
                password=self.database_password,
                database=self.database_name
            )
            return connection
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None
    
    def get_data(self, query, params=None):
        connection = self.get_connection()
        if connection is None:
            return None
        
        try:
            cursor = connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
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
            cursor = connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchone()
            return result
        except Error as e:
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
        except Error as e:
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
        except Error as e:
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
        except Error as e:
            print(f"Error deleting data: {e}")
            connection.rollback()
            return 0
        finally:
            cursor.close()
            connection.close()

# Singleton instance
db = DatabaseHelper()

# Other configurations
SECRET_KEY = "your-secret-key-here"
JWT_EXPIRY = 3600  # 1 hour