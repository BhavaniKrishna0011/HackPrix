import time
import os
import sqlite3
from flask import Flask, jsonify, request
from werkzeug.serving import make_server
import threading

DB_FILE = 'dataset.db'

def create_app():
    app = Flask(__name__)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Create separate tables for clothing, sports, and vehicles
    c.execute('''CREATE TABLE IF NOT EXISTS clothing
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS sports
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS vehicles
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT)''')

    conn.commit()
    conn.close()

    @app.route('/dataset', methods=['GET'])
    def get_dataset():
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT * FROM clothing")
        clothing = c.fetchall()
        c.execute("SELECT * FROM sports")
        sports = c.fetchall()
        c.execute("SELECT * FROM vehicles")
        vehicles = c.fetchall()
        conn.close()
        return jsonify({"clothing": clothing, "sports": sports, "vehicles": vehicles})

    @app.route('/dataset', methods=['POST'])
    def update_dataset():
        data_type = request.form['type']
        url = request.form['url']
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        if data_type.lower() == 'clothing':
            c.execute("INSERT INTO clothing (url) VALUES (?)", (url,))
        elif data_type.lower() == 'sports':
            c.execute("INSERT INTO sports (url) VALUES (?)", (url,))
        elif data_type.lower() == 'vehicle':
            c.execute("INSERT INTO vehicles (url) VALUES (?)", (url,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 201

    return app

class ServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.server = make_server('0.0.0.0', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print("Starting server")
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

def check_temp_file():
    temp_file_path = 'temp_data.txt'
    while True:
        if os.path.exists(temp_file_path):
            try:
                with open(temp_file_path, 'r') as temp_file:
                    data = temp_file.read().strip()
                    if data:
                        data_type, url = data.split(',')
                        # Insert data into the appropriate table based on data type
                        conn = sqlite3.connect(DB_FILE)
                        c = conn.cursor()
                        if data_type.lower() == 'clothing':
                            c.execute("INSERT INTO clothing (url) VALUES (?)", (url,))
                        elif data_type.lower() == 'sports':
                            c.execute("INSERT INTO sports (url) VALUES (?)", (url,))
                        elif data_type.lower() == 'vehicle':
                            c.execute("INSERT INTO vehicles (url) VALUES (?)", (url,))
                        conn.commit()
                        conn.close()
                        print(f"Added: Type: {data_type} | URL: {url}")
                os.remove(temp_file_path)
            except Exception as e:
                print(f"Error reading from temp file: {e}")
        time.sleep(2)  # Check the file every 2 seconds

def main():
    app = create_app()
    server_thread = ServerThread(app)
    server_thread.start()
    print(f"Flask server running in thread with PID: {os.getpid()}")

    # Run the file checking in the main process
    try:
        check_temp_file()
    except KeyboardInterrupt:
        print("Exiting...")
        server_thread.shutdown()
        server_thread.join()
        exit(0)

if __name__ == '__main__':
    main()
