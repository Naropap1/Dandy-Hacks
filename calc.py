# do the math stuff here i guess?
#
import math

### IDEAL NAP TIMES (by priority)
#
# 90-120 min => full, deep, REM sleep
#
# 45 min => upper bounds on nap before 90 min. DO NOT go b/w 45 and 90 min
#
# 20 min=> power nap! Not fully resting, but makes you more alert & awake


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
#assuming value between 0 and 24
def hour_converter(hours):
	return min_converter(hours*60)

#converts minutes to 5-minute intervals
#assuming value between 0 and 1440
def min_converter(minutes):
	return (minutes/5)

#Find your ideal time of day for a nap! Depends on user's sleeping schedule
def nap_zone(sleeptime, waketime):
	normfactor = 51.2
	goal = 4.67*((sleeptime+waketime)/2)-normfactor