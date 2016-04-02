# do the math stuff here i guess?
#
import math

### IDEAL NAP TIMES
#
# 90-120 min => full, deep, REM sleep
#
# 45 min => upper bounds on nap before 90 min. DO NOT go b/w 45 and 90 min for good rest
#
# 60 min => best for memory writing/remembering things. Leaves you groggy when you wake up though
#
# 20 min=> power nap! Not fully resting, but makes you more alert & awake


#boolean array of 5-minute intervals, tells whether or not this person is free at that time
occupied = [288]
travel_time = 0


#boolean function to find if a given time interval is comepletely free
#NOTE: times are represented in 5 minute intervals
def is_free(occupied, start_time, length):
	freeness = True
	for x in range(start_time, start_time+length):
		try:
			if occupied[x]: freeness = False
			break
		except IndexError
			pass
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

def freetimes(occupied):
	free_times=[] #array with timestamp for beginning of each "free" block
	for x in range(0,288)
		if is_free(occupied, x, 4): #only check for at least 20 minutes of free time
			free_times.append(x)
	return free_times

#finds all possible nap start times for each type of nap
def possible_naps(occupied):

	possible_times = freetimes(occupied)

	power_naps=[]  #possible 20 min naps
	for i in range(len(possible_times))
		if is_free(occupied, possible_times[i], 4):
			power_naps.append(possible_times[i])
	short_naps=[]  #possible 45 min naps
	for i in range(len(possible_times))
		if is_free(occupied, possible_times[i], 9):
			power_naps.append(possible_times[i])
	memory_naps=[] #possible 60 min naps
	for i in range(len(possible_times))
		if is_free(occupied, possible_times[i], 8):
			power_naps.append(possible_times[i])
	rest_naps=[]   #possible 90 min naps
	for i in range(len(possible_times))
		if is_free(occupied, possible_times[i], 18):
			power_naps.append(possible_times[i])