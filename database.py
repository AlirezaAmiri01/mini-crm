import sqlite3

def create_connection():
    connection = sqlite3.connect("crm.db")
    connection.execute("PRAGMA foreign_keys = ON")

    return connection


def create_customers_table(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    company TEXT,
    position TEXT,
    registered_at TEXT,
    notes TEXT
    )
    
    """)



def create_intractions_table(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS intractions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL ,
    type TEXT NOT NULL,
    date TEXT NOT NULL,
    subject TEXT NOT NULL,
    notes TEXT NOT NULL,
    result TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    )  
    """)


def create_follow_ups_table(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS fllowups(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    date TEXT,
    subject TEXT,
    description TEXT,
    status TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
    """)


if __name__ == "__main__":
    connection = create_connection()
    create_customers_table(connection)
    create_intractions_table(connection)
    create_follow_ups_table(connection)
    connection.commit()
    connection.close()
    print("All tables created successfully")