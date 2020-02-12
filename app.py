from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    # data = request.data.decode("utf8")
    # print(data)
    # print(data["chat"]["id"])
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
