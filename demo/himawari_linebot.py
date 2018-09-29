# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import os
import sys
from argparse import ArgumentParser
from flask import Flask, request, abort, jsonify, Response

import diagnosis
import radar_graph
import line_graph

import json

app = Flask(__name__)

@app.route("/linebot", methods=['GET'])
def callback():

    jfile = open("sensor.json","r")
    sensor = json.load(jfile)
    jfile.close()

    print(sensor)

    anger_hist = sensor["hist"]
    anger_data = sensor["data"]
    diag_list = ["",""]

    diagnosis.check(anger_data,diag_list)
    print(diag_list)

    radar_graph.create_radar_graph(anger_data)
    line_graph.create_line_graph(anger_hist)

    response = Response(
        response=json.dumps(diag_list),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route('/get_image/<filename>/<token>')
def get_image(filename, token):
    from flask import send_file
    # print(filename)
    # filename = filename + '.jpg'
    return send_file(filename + '.jpg', mimetype='image/jpg')

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
