import json
import os

from flask import Flask, request, make_response, jsonify

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)

appdata_dir = os.path.abspath('/var/lib/appdata')
data_file_name = os.path.join(appdata_dir, 'companies.json')


@app.route('/')
def default_msg():
    return 'hello'


@app.route('/echo/<x>/')
def root(x='megatron'):
    print('\nekoing...\n\n')
    return 'OMG! Its {}!\n'.format(x)


@app.route('/companies/')
def data():
    try:
        data_file = json.load(open(data_file_name, 'rt'))
    except IOError:
        print('tried to open {}'.format(data_file_name))
        data_file = {}

    return make_response(
        jsonify(data_file),
        200,
        {
            'Content-Type': 'application/json',
            'X-Powered-By': 'Magic'
        }
    )


@app.route('/cors/', methods=['GET'])
def echo():
    headers = {
        # Set Headers (GENERAL)
        'Content-Type': 'application/json',
        'X-Powered-By': 'Magic',
        # Set Headers (CORS)
        'Access-Control-Allow-Origin': "*",
        'Access-Control-Allow-Methods': 'HEAD, GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Origin Accept Content-Type X-Requested-With X-CSRF-Token',
    }

    search_text = request.args.get('q', '').strip()
    return make_response(jsonify(message=search_text), 200, headers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
