# Não consegui usar o endpoint do sentimento :(

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/1.0/api")
def v1():
    return "This is V1"

@app.route("/2.0/api")
def v2():
    return "This is V2"

if __name__ == "__main__":
    app.run(debug=True)


