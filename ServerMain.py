import signal
import sys
from flask import Flask, jsonify

app = Flask(__name__)

# Static sample dataset containing type and URL pairs, focusing on clothing and sports
sample_dataset = [
    ["clothing", "http://example.com/clothing1.jpg"],
    ["clothing", "http://example.com/clothing2.jpg"],
    ["clothing", "http://example.com/clothing3.jpg"],
    ["clothing", "http://example.com/clothing4.jpg"],
    ["clothing", "http://example.com/clothing5.jpg"],
    ["sports", "http://example.com/sports1.jpg"],
    ["sports", "http://example.com/sports2.jpg"],
    ["sports", "http://example.com/sports3.jpg"],
    ["sports", "http://example.com/sports4.jpg"],
    ["sports", "http://example.com/sports5.jpg"],
    ["clothing", "http://example.com/clothing6.jpg"],
    ["clothing", "http://example.com/clothing7.jpg"],
    ["sports", "http://example.com/sports6.jpg"],
    ["sports", "http://example.com/sports7.jpg"],
    ["clothing", "http://example.com/clothing8.jpg"],
    ["sports", "http://example.com/sports8.jpg"],
    ["image", "http://example.com/image1.jpg"],
    ["video", "http://example.com/video1.mp4"],
    ["document", "http://example.com/document1.pdf"],
    ["audio", "http://example.com/audio1.mp3"],
]

@app.route('/dataset', methods=['POST'])
def get_dataset():
    # Logic to handle POST request
    print("Received POST request")
    print("Sample Dataset:")
    for data in sample_dataset:
        print("Type:", data[0], "| URL:", data[1])
    
    # Respond with the dataset
    return jsonify(sample_dataset)

def handle_signal(sig, frame):
    print(f"Signal {sig} received. Running the program...")
    print("Sample Dataset:")
    for data in sample_dataset:
        print("Type:", data[0], "| URL:", data[1])
    # This is where you can add more functionality if needed

# Register the signal handler for SIGUSR1
signal.signal(signal.SIGUSR1, handle_signal)

if __name__ == '__main__':
    # Run the Flask server in a separate process
    from multiprocessing import Process
    server = Process(target=app.run, kwargs={'debug': True, 'host': '0.0.0.0', 'port': 5000})
    server.start()

    print(f"Python process PID: {server.pid}")

    # Keep the main process alive to listen for signals
    try:
        while True:
            signal.pause()  # Wait for signals
    except KeyboardInterrupt:
        print("Exiting...")
        server.terminate()
        sys.exit(0)
