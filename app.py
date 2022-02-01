#!/usr/bin/env python3
import sys
from flask import Flask
from flask import  jsonify
from flask import Response

app = Flask(__name__)

dictionnaire = {"message": "hello world"}

@app.route("/")
def hello():
	if len(sys.argv) >= 3:
		dictionnaire["message"]=str(sys.argv[2])
		return jsonify(dictionnaire)
	else:
		return jsonify(dictionnaire)


if __name__ == '__main__':
	if len(sys.argv) >= 2:
		app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
	else :
		app.run(host='0.0.0.0',port=5000, debug=True)
