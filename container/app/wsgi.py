from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Asking for home')
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/echo_request')
def echo_request():
    app.logger.info('Asking for home')
    return jsonify(dict(request.headers))

@app.route('/fail')
def fail_request():
    raise Exception("Very bad")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')