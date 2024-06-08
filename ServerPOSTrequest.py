import sqlite3
import random
import requests

DB_FILE = 'dataset.db'

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

def send_urls_to_destination(clothing_url, sports_url, vehicle_url):
    destination_ip = '192.168.241.164:8000'

    # Send URLs to destination IP address
    if clothing_url:
        requests.post(f'http://{destination_ip}', data={'type': 'clothing', 'url': clothing_url})
    if sports_url:
        requests.post(f'http://{destination_ip}', data={'type': 'sports', 'url': sports_url})
    if vehicle_url:
        requests.post(f'http://{destination_ip}', data={'type': 'vehicle', 'url': vehicle_url})

def main():
    clothing_url, sports_url, vehicle_url = fetch_random_urls()
    send_urls_to_destination(clothing_url, sports_url, vehicle_url)

if __name__ == '__main__':
    main()
