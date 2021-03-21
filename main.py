import random
import string
import requests

from flask import Flask, render_template

from faker import Faker


fake = Faker()
app = Flask(__name__)


@app.route('/password/generate')
def password_generate():
    passwd = ""
    for _ in range(10):
        passwd += random.choice(string.digits)
    return render_template('main.html', password=passwd)


@app.route('/user/generate')
def user_generate():
    res = ""
    for _ in range(20):
        res += str(fake.name()) + ';' + str(fake.free_email()) + ';\n'
    return res


@app.route('/astro')
def astro():
    response = requests.get('http://api.open-notify.org/astros.json', json={'number': 'value'})
    json_response = response.json()
    return str(json_response['number'])




