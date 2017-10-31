from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"]) 
def signup():
	return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
	return render_template("signin.html")

if __name__ == "__main__":
	app.run(debug=True)