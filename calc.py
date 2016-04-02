# do the math stuff here i guess?
#
import math

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