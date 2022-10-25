from flask import Flask, render_template
from flask_cors import CORS
from api.api import api as api

app = Flask(__name__, static_folder="templates")


@app.route('/')
@app.route('/index')
def hello_world():  # put application's code here
    return render_template("index.html")


CORS(app, support_credentials=True)

app.register_blueprint(api)


if __name__ == '__main__':
    app.run(debug=True)
