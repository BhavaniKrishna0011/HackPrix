from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data_type = request.form['type']
    url = request.form['url']
    print(f"Received data from server - Type: {data_type}, URL: {url}")
    return 'Data received successfully'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
