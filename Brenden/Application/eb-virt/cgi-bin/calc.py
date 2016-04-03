#! D:\Python27\python.exe

# do the math stuff here i guess?


import math

# ***********************************************************************
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
	
# *************************************************************************
# copy this section to the end of your calculations with values inserted where needed
# this is what "returns" the data to the web page as a pre-built html page
# modify this section as if you were writing an html page if necessary
print "Content-Type: test/html"
print

######### napstring should be something like "you should nap from <calculated begin> to <calculated end>"
# you can also just re-write this to reflect whatever html you want
print "<p>" + napstring + "</p>"

######### substitute the nap instructions string in for insrtuctions here
print "<p>" + instructions + "</p>"

######### substitute the benefits string in here
print "<p>" + benefits + "<p>"

# *************************************************************************
	
