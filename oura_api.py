from flask import Flask, jsonify
from auth import get_oura_client

app = Flask(__name__)

@app.route('/personal-info', methods=['GET'])
def personal_info():
    client = get_oura_client()
    info = client.get_personal_info()
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True) 