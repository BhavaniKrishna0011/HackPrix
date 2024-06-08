import requests
import random

def fetch_random_url(base_url, table_name):
    response = requests.get(f"{base_url}/dataset")
    data = response.json()
    if table_name in data and data[table_name]:
        return random.choice(data[table_name])[1]  # [1] to get the URL from the tuple (id, url)
    return None

def main():
    base_url = "http://192.168.241.164:5000"  # Change this to your server's IP and port

    clothing_url = fetch_random_url(base_url, 'clothing')
    sports_url = fetch_random_url(base_url, 'sports')
    vehicles_url = fetch_random_url(base_url, 'vehicles')

    print(f"Clothing URL: {clothing_url}")
    print(f"Sports URL: {sports_url}")
    print(f"Vehicles URL: {vehicles_url}")

    # Assuming you want to send these URLs to another server
    destination_url = "http://192.168.241.164:8000"  # Change this to your destination server's URL
    payload = {
        "clothing_url": clothing_url,
        "sports_url": sports_url,
        "vehicles_url": vehicles_url
    }
    response = requests.post(destination_url, json=payload)
    print(f"Response from destination: {response.status_code}, {response.text}")

if __name__ == '__main__':
    main()
