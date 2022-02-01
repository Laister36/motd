from flask import Flask
from flask import  jsonify
app = Flask(__name__)

@app.route("/")
def hello():
	d = "<p>Hello World!</p>"
	return jsonify(d)


if __name__ == '__main__':
    app.run(host="10.0.2.15", port=8000, debug=True)
