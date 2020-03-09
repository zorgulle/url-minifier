from minifyer.minifyer import Minifyer
from encoder.encoder import Base64EncoderStrategy

from flask import request
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/minify', methods=['POST'])
def minify():
    minifyier = Minifyer(Base64EncoderStrategy())
    result = minifyier.minify(request.json['url'])

    return {"result": result}


@app.route('/deminify', methods=['POST'])
def deminify():
    minifyier = Minifyer(Base64EncoderStrategy())
    result = minifyier.deminify(request.json['url'])

    return {"result": result}


@app.route('/', methods=['GET'])
def index():
    return {"message": "OK"}

def start():
    app.run('0.0.0.0', debug=True)