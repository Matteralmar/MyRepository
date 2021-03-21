import random
import string
import requests

from flask import Flask, render_template

from faker import Faker


fake = Faker()
app = Flask(__name__)


@app.route('/password/generate')
@app.route('/password/generate/<int:number>')
def password_generate(number=20):
    passwd = ""
    for _ in range(number):
        passwd += random.choice(string.digits)

    return render_template('main.html', password=passwd)


@app.route('/user/generate')
@app.route('/user/generate/<int:n>')
def user_generate(n=10):
    res = ""
    for _ in range(n):
        res += str(fake.name()) + ';' + str(fake.free_email()) + ';\n'
    return res


@app.route('/astro')
def astro():
    response = requests.get('http://api.open-notify.org/astros.json', json={'number': 'value'})
    json_response = response.json()
    return str(json_response['number'])
