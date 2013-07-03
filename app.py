#!/usr/bin/python

import proximity
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return str(prox.checkProximity())

if __name__ == '__main__':
	prox = proximity.Proximity()
	prox.setup()
	app.run(host = '0.0.0.0', debug = True, port = 8080)
