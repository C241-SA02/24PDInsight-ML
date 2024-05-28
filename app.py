from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

# Line for Check the code
if __name__ == '__main__':
    app.run(debug=True)