from flask import Flask,json, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/test')
def test():
    person={
        "name":"ashu",
        "age": 12
    }
    response = app.response_class(
        response=json.dumps(person),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/send", methods=["POST"])
def send():
    data=request.json
    return data


if __name__ == '__main__':
    app.run(debug=True)