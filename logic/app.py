import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_statistics():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
    
