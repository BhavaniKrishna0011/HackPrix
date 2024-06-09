import requests

def send_get_request():
    server_url = ' http://192.168.241.164:8001/trigger_post'
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            print("GET request sent successfully")
        else:
            print(f"Failed to send GET request. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    send_get_request()
