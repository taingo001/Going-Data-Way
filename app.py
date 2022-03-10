from flask import Flask, render_template, request, flash, send_file
import csv

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

# Create a route for index.html/ home page
"""@app.route("/")
def index():
	return render_template("index.html")"""

@app.route('/', methods=["GET", "POST"])
def index():
    data = []
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['filename'] # This line uses the same variable and worked fine
            filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
            uploaded_file.save(filepath)
            with open(filepath) as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    data.append(row)
            return redirect(request.url)
    return render_template('index.html', data=data)

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

#@app.route("/data", methods=['GET', 'POST'])
#def data():
	#if request.method == 'POST':
		#f = request.form['csv file']
		#data = []
		#with open(f) as file:
			#csvfile = csv.reader(file)
			#for row in csvfile:
				#data.append(row)
		#data = pd.DataFrame(data)
		#return render_template("data.html", data=data.to_html(header=False, index=False))


@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
