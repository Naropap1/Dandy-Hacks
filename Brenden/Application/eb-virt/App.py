# do the math stuff here i guess?

from flask import Flask, json, jsonify, request
app = Flask(__name__)
import math

@app.route("/")
def main():
	return render_template('index.html')
	
@app.route('/nap', methods = ['POST'])
def getNap():
	#this is just the times list, first two are sleep begin and end
	#add any other parameters here - get these from 'data' portion of ajax call
	#ex. request.form['test'] would get the test field of data, and then pass these in to calculate
	times = request.form['times']
	values = calc(times) #add any other parameters
	return jsonify(results = values)
	
if __name__ == "__main__":
    app.run()
	

# ***********************************************************************
# this is the non-flask stuff, so don't use it
# copy this section to get values as a string array
import json
import cgitb
cgitb.enable()

import cgi
data = cgi.FieldStorage()
times = json.loads(data["times"].value)

# times is the string array
# ************************************************************************

#boolean array of 5-minute intervals, tells whether or not this person is free at that time
occupied = [288]

#boolean function to find if a given time interval is comepletely free
#NOTE: times are represented in 5 minute intervals
def is_free(occupied, nap_interval):
	freeness = True
	for x in range(nap_interval[0], nap_interval[1]):
		if occupied [x]: freeness = False
	return freeness

#converts hours to 5-minute intervals
def hour_converter(hours):
	return min_converter(hours*60)

#converts minutes to 5-minute intervals
def min_converter(minutes):
	return (minutes/5)
	

	
