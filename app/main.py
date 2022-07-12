from flask import Flask
from modules.model.main import run_model

app = Flask(__name__)

@app.route("/", methods=['POST'])
def post():
    response = json.loads(request.data)
    arrayStr = response['array'].split(',')
    arrayInt = list(map(int, arrayStr))
    result = run_model(X_train, X_test, y_train, y_test, arrayInt)

    return str(result)

@app.route("/", methods=['GET'])
def get():
    return "<p>Hello, World!</p>"