import json
import os

from flask import Flask

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)

appdata_dir = os.path.abspath('/var/lib/appdata')
data_file_name = os.path.join(appdata_dir, 'companies.json')


@app.route('/data/x')
def data():
    try:
        data_file = json.load(open(data_file_name, 'rt'))
    except IOError:
        print('tried to open {}'.format(data_file_name))
        data_file = {}
    return json.dumps(data_file, indent=2)


@app.route('/')
def default_msg():
    return 'hello'


@app.route('/<x>')
def root(x='megatron'):
    print('\n\nhello..\n\n')
    return 'OMG! Its {}!\n'.format(x)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
