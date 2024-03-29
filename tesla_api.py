# https://github.com/tdorssers/TeslaPy

import os
import teslapy
from flask import Flask, json
from flask_cors import CORS, cross_origin
from waitress import serve

# EMAIL = os.getenv("REACT_APP_EMAIL")
EMAIL = 'john@rimell.cc'

app = Flask(__name__, static_folder='./build', static_url_path='')
CORS(app, headers='Content-Type')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route("/vehicle_data", methods=["GET"])
def getData():
    with teslapy.Tesla(EMAIL) as tesla:
        vehicles = tesla.vehicle_list()
        vehicles[0].sync_wake_up()

        # vehicles[0].command('ACTUATE_TRUNK', which_trunk='front')
        # print(vehicles[0].get_vehicle_data()['vehicle_state']['car_version'])

        # print(vehicles[0].get_vehicle_data())
        try:
            return json.dumps(vehicles[0].get_vehicle_data())
        except:
            print('failed')
        # return vehicles[0].get_vehicle_data()


serve(app, port=5000) # serve app in production
# app.run(port=5000) # serve app in development