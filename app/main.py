from flask import Flask
import json
from flask import request
from modules.model.main import run_model
from modules.training.main import training

app = Flask(__name__)


@app.route("/", methods=['POST'])
def post():
    response = json.loads(request.data)
    arrayStr = response['array'].split(',')
    arrayInt = list(map(int, arrayStr))

    if len(arrayInt) != 10:
        return 'array tidak sesuai format'

    result = run_model(X_train, X_test, y_train, y_test, arrayInt)
    print(result)

    return str(result)

@app.route("/", methods=['GET'])
def get():
    global X_train, X_test, y_train, y_test

    X_train, X_test, y_train, y_test = training()
    
    return "Service is running"