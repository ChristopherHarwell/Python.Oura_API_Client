from flask import Flask, jsonify, request
from auth import get_oura_client

app = Flask(__name__)

@app.route('/personal-info', methods=['GET'])
def personal_info():
    client = get_oura_client()
    info = client.get_personal_info()
    return jsonify(info)

@app.route('/daily-sleep', methods=['GET'])
def daily_sleep():
    client = get_oura_client()
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    sleep_data = client.get_daily_sleep(start_date=start_date, end_date=end_date)
    return jsonify(sleep_data)

if __name__ == '__main__':
    app.run(debug=True) 