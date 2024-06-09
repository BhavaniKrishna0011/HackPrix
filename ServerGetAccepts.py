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

    c.execute("SELECT url FROM electronics ORDER BY RANDOM() LIMIT 1")
    electronics_result = c.fetchone()
    electronics_url = electronics_result[0] if electronics_result else None

    c.execute("SELECT url FROM vehicles ORDER BY RANDOM() LIMIT 1")
    vehicle_result = c.fetchone()
    vehicle_url = vehicle_result[0] if vehicle_result else None

    conn.close()
    return clothing_url, electronics_url, vehicle_url


@app.route('/trigger_post', methods=['GET'])
def trigger_post():
    # Try to get the real IP address if behind a proxy
    if request.headers.get('X-Forwarded-For'):
        client_ip = request.headers.getlist('X-Forwarded-For')[0]
    else:
        client_ip = request.remote_addr

    clothing_url, electronics_url, vehicle_url = fetch_random_urls()

    # Log the client IP and fetched URLs for debugging
    app.logger.info(f"Client IP: {client_ip}")
    app.logger.info(f"Fetched URLs: Clothing: {clothing_url}, Electronics: {electronics_url}, Vehicles: {vehicle_url}")

    # Assume the client is prepared to receive the POST request (for testing purposes)
    try:
        response = requests.post(f'http://{client_ip}:8000', json=[
            {'type': 'Clothing', 'url': clothing_url},
            {'type': 'Electronics', 'url': electronics_url},
            {'type': 'Vehicles', 'url': vehicle_url}
        ])
        app.logger.info(f"POST response: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Failed to send POST request to {client_ip}:8000 - {e}")
        return jsonify({"status": "Failed to send POST request", "error": str(e)}), 500

    return jsonify({"status": "GET request received", "client_ip": client_ip}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)
