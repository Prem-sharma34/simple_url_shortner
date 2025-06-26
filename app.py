from flask import Flask


app = Flask(__name__)


app.route("/")
def Home():
    return "Welcome to Home page"






if __name__ == "main":
    app.run(debug=True)