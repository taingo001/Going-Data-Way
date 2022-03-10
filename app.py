from flask import Flask, render_template, request, flash, send_file
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

# Create a route for Download button so that users can download the template csv file
@app.route('/csv_template.csv') # this is a job for GET, not POST
def download_csv():
    return send_file('csv_template.csv',
                     mimetype='text/csv',
                     attachment_filename='csv_template.csv',
                     as_attachment=True)

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
