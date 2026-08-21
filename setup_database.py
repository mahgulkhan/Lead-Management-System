import sqlite3
import os

def create_tables():
    # Connect to SQLite database (creates if not exists)
    conn = sqlite3.connect('lead_management.db')
    cursor = conn.cursor()
    
    # Create admin_users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin_users (
            admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create leads table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            lead_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            contact_name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            message TEXT,
            source TEXT DEFAULT 'Website',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create audit_log table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audit_log (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_id INTEGER,
            admin_id INTEGER,
            action TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert a default admin user (username: admin, password: admin123)
    # Note: In production, use a proper password hash!
    cursor.execute('''
        INSERT OR IGNORE INTO admin_users (username, password_hash, email)
        VALUES ('admin', 'admin123', 'admin@localhost')
    ''')
    
    conn.commit()
    conn.close()
    print("Database created successfully!")
    print("Default admin: username='admin', password='admin123'")

if __name__ == '__main__':
    create_tables()