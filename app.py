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

@app.route("/data", methods=['GET', 'POST'])
def data():	
		#Ask what file to read--simulate uploading file
		FILENAME=input("What file would you like to read? ")

		#Read file and output the file headers
		with open(FILENAME, mode='r') as csv_file:
		    csvFile = csv.reader(csv_file)
		    reader = csv.reader(csv_file)
		    headers = next(reader)
		    print(', '.join(headers))

		#Get user input
		selected = []
		selected = input("What section(s) would you like to focus on?\nEnter here: ").split()

		#Print new line
		print('\n')

		#Use input to print the selected columns
		with open(FILENAME, newline="") as csvfile:
		    data = list(csv.DictReader(csvfile))
		    for element in selected:
			print(element)  # print selected header
			print("---------------------------------")
			for column in data:  
			    print(column[element])  # print data
			print("\n")


		# Calculate Averages for selected column
		def average():
		  sum = []
		  for element in range(len(column[element]))
		  sum += int(column[element])
		  print(sum/len(column[element]))
		# Calculate Income

		#Calculate Accounts Receivable
		return render_template("data.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
