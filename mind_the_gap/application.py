from flask import Flask
from flask import render_template
from tbm import extract_info, get_info

app = Flask(__name__)

#@app.route('/hello/')
#@app.route('/hello/<name>')
@app.route('/')
def hello(name=None):
    return render_template('display.html',
                           name=extract_info(get_info()))
