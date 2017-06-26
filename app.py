from flask import Flask, render_template, redirect, request, jsonify
from pymongo import MongoClient
import jinja2
import csv

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROPAGATE_EXCEPTIONS'] = True
from kickoff import run_kickoff

# ROUTES:

start = "2017-05-10"
end = "2017-05-31"

@app.route('/')
def index():
	return redirect('/dashboard')

@app.route('/kickoff', methods = ['GET','POST'])
def kickoff():
	run_kickoff(start, end)
	businesses =[b for b in db.summaries.find()]
	return render_template('index.html.jinja', businesses = businesses)

@app.route('/dashboard')
def dashboard():
	# get list of business names/ids from mongo
	businesses =[b for b in db.summaries.find()]
	return render_template('index.html.jinja', businesses = businesses)

@app.route('/summaries/<b_id>')
def summary(b_id):
	summary = db.summaries.find_one({'business_id': b_id})
	return render_template('summary.html.jinja', summary=summary)

@app.route('/processdate', methods = ['POST'])
def processdate():
	global start
	start = request.json["start"]
	global end
	end = request.json["end"]
	businesses =[b for b in db.summaries.find()]
	return render_template('index.html.jinja', businesses = businesses)

@app.route('/aspect', methods=['POST'])
def aspect():

	if request.method == 'POST':
		a = request.form['aspect']
		if version:
			with open('logs/aspects.csv', 'wb') as f:
				writer = csv.writer(f)
				writer.writerow([a])
			businesses =[b for b in db.summaries.find()]
			return render_template('index.html.jinja', businesses = businesses)

	return jsonify ({'error': 'the aspects you entered is not in the correct format, please separate by comma'})

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html.jinja')
    return jsonify({'error': 'Please upload only csv file!'})

@app.route('/overview/<b_id>')
def overview(b_id):
	summary = db.summaries.find_one({'business_id': b_id})
	return render_template('overview.html.jinja', summary=summary)


@app.template_filter()
def less_than_ten(number):
	return number <= 10

if __name__ == "__main__":

	# Setup db connection
	client = MongoClient()
	db = client.rnwtest2
	print "Connected to Mongo database"

	app.jinja_env.filters['less_than_ten'] = less_than_ten

	app.run(host='127.0.0.1', port=54770, debug=True)
