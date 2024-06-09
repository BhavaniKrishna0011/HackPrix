import sqlite3

DB_FILE = 'dataset.db'
TEXT_FILE = 'temp_data1.txt'

# def create_tables():
#     conn = sqlite3.connect(DB_FILE)
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS clothing (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             url TEXT NOT NULL
#         )
#     ''')
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS electronics (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             url TEXT NOT NULL
#         )
#     ''')
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS vehicles (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             url TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

def insert_data_from_file(file_path):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(',', 1)
                if len(parts) == 2:
                    data_type = parts[0].strip().lower()
                    url = parts[1].strip()
                    
                    if data_type == 'clothing':
                        c.execute("INSERT INTO clothing (url) VALUES (?)", (url,))
                    elif data_type == 'electronics':
                        c.execute("INSERT INTO electronics (url) VALUES (?)", (url,))
                    elif data_type == 'vehicle':
                        c.execute("INSERT INTO vehicles (url) VALUES (?)", (url,))
                    else:
                        print(f"Unknown type: {data_type}")
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # create_tables()
    insert_data_from_file(TEXT_FILE)
