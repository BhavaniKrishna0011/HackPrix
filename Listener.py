from flask import Flask, request, jsonify
import sys
app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received data: {data}")
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)