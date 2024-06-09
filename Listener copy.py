from flask import Flask, request, jsonify
import json
import os
import requests
import schedule
import time
import threading
from queue import Queue

app = Flask(__name__)

# Ensure the output directory exists
output_directory = 'output'
os.makedirs(output_directory, exist_ok=True)

# Create a queue to handle JSON data
data_queue = Queue()

@app.route('/', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received data: {data}")
    
    # Put the received JSON data in the queue
    data_queue.put(data)

    return jsonify({"status": "received"}), 200

def send_get_request():
    server_url = 'http://192.168.241.164:8001/trigger_post'  # Change this to your server URL
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            print("GET request sent successfully")
        else:
            print(f"Failed to send GET request. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Schedule the job to send the GET request every 3 seconds
schedule.every(3).seconds.do(send_get_request)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def process_queue():
    output_file_path = os.path.join(output_directory, 'data.json')
    while True:
        data = data_queue.get()
        with open(output_file_path, 'w') as json_file:
            json.dump(data, json_file)
        data_queue.task_done()

if __name__ == '__main__':
    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()

    # Start the queue processor in a separate thread
    queue_thread = threading.Thread(target=process_queue, daemon=True)
    queue_thread.start()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=8000)
