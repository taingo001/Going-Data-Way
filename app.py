from flask import Flask, render_template, request, flash
import csv

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

# Create a route for index.html/ home page
@app.route("/")
def index():
	return render_template("index.html")

# Create a route for about.html/ about page
@app.route("/about")
def about():
	return render_template("about.html")

# Create a route for help.html/ help page
@app.route("/help")
def help():
	return render_template("help.html")

@app.route("/download")
def download():
	p = "test-file.text"
	return send_file(p,as_attachment=True)

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
