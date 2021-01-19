from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello World!"


@app.route("/TEST")
def hello_test():
    return "Hello TEST!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)