from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
	return render_template("home/index.html")

@app.route("/find")
def find():
	return render_template("find/index.html")

if __name__ == "__main__":
	app.run()
