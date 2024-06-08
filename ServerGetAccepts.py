from flask import Flask, jsonify, request
import sqlite3
import random
import requests

DB_FILE = 'dataset.db'

app = Flask(__name__)

def fetch_random_urls():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Fetch one random URL from each table
    c.execute("SELECT url FROM clothing ORDER BY RANDOM() LIMIT 1")
    clothing_result = c.fetchone()
    clothing_url = clothing_result[0] if clothing_result else None

    c.execute("SELECT url FROM sports ORDER BY RANDOM() LIMIT 1")
    sports_result = c.fetchone()
    sports_url = sports_result[0] if sports_result else None

    c.execute("SELECT url FROM vehicles ORDER BY RANDOM() LIMIT 1")
    vehicle_result = c.fetchone()
    vehicle_url = vehicle_result[0] if vehicle_result else None

    conn.close()
    return clothing_url, sports_url, vehicle_url

@app.route('/trigger_post', methods=['GET'])
def trigger_post():
    clothing_url, sports_url, vehicle_url = fetch_random_urls()
    destination_ip = '192.168.241.164:8000/'

    # Send URLs to destination IP address
    requests.post(f'http://{destination_ip}', json=[{'type': 'clothing', 'url': clothing_url},{'type': 'sports', 'url': sports_url},{'type': 'vehicle', 'url': vehicle_url}])

    return jsonify({"status": "GET request received"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)
