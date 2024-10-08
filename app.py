import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Working"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
