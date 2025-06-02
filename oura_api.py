from flask import Flask, jsonify, request
from auth import get_oura_client

class OuraAPI:
    def __init__(self):
        self.client = get_oura_client()
        self.app = Flask(__name__)
        self.register_routes()

    def register_routes(self):
        @self.app.route('/personal-info', methods=['GET'])
        def personal_info():
            info = self.client.get_personal_info()
            return jsonify(info)

        @self.app.route('/daily-sleep', methods=['GET'])
        def daily_sleep():
            start_date = request.args.get('start_date')
            end_date = request.args.get('end_date')
            sleep_data = self.client.get_daily_sleep(start_date=start_date, end_date=end_date)
            return jsonify(sleep_data)

oura_api = OuraAPI()
app = oura_api.app

if __name__ == '__main__':
    app.run(debug=True) 