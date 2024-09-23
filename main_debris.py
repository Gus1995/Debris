import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    User_ID INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    institution TEXT
);
''')

def insert_value(user_id, first_name, last_name, email, institution):
    cursor.execute("SELECT * FROM User WHERE email = ?", (email,))
    
    if cursor.fetchone():
        print("User already exists.")
    else:
        query = '''INSERT INTO User (User_ID, first_name, last_name, email, institution)
                   VALUES (?, ?, ?, ?, ?)'''
        cursor.execute(query, (user_id, first_name, last_name, email, institution))
        print("User inserted.")

def delete_value(user_id, table):
    cursor.execute("DELETE FROM "+table+" WHERE User_ID = "+str(user_id)+";")
    

def retrieve(table):
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()

    for row in rows:
        print(row)


insert_value(888, "Gustavo", "Luis", "ff.ff.com", "CIBC")

delete_value(777, "User")
retrieve('User')
conn.commit()
conn.close()
