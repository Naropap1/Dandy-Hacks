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
occupied = [False]*288
travel_time = 0
nap_type = 0 #0=no emphasis, 1=power nap, 2=rest nap, 3=study nap

#boolean function to find if a given time interval is comepletely free
#NOTE: times are represented in 5 minute intervals
def is_free(occupied, start_time, length):
	freeness = True
	for x in range(start_time, start_time+length):
		try:
			if occupied[x]: freeness = False
			break
		except IndexError:
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
	for x in range(0,288):
		if is_free(occupied, x, 4): #only check for at least 20 minutes of free time
			free_times.append(x)
	return free_times

#finds all possible nap start times for each type of nap
def possible_naps(occupied):

	possible_times = freetimes(occupied)

	power_naps=[]  #possible 20 min naps
	for i in range(len(possible_times)):
		if is_free(occupied, possible_times[i], 4):
			power_naps.append(possible_times[i])
	short_naps=[]  #possible 45 min naps
	for i in range(len(possible_times)):
		if is_free(occupied, possible_times[i], 9):
			short_naps.append(possible_times[i])
	study_naps=[] #possible 60 min naps
	for i in range(len(possible_times)):
		if is_free(occupied, possible_times[i], 12):
			study_naps.append(possible_times[i])
	rest_naps=[]   #possible 90 min naps
	for i in range(len(possible_times)):
		if is_free(occupied, possible_times[i], 18):
			rest_naps.append(possible_times[i])

def best_nap(occupied, focus):

	possible_naps(occupied)

	if focus == 1:			#power naps
		pwr_weight = 3
		rst_weight = 1.5
		shrt_weight= 1
		stdy_weight= 1
	elif focus == 2:		#rest naps
		pwr_weight = 1.5
		rst_weight = 3
		shrt_weight= 0.5
		stdy_weight= 0.5
	elif focus == 3:		#study naps
		pwr_weight = 1
		rst_weight = 1.5
		shrt_weight= 2
		stdy_weight= 3
	else:					#no emphasis
		pwr_weight = 1
		rst_weight = 1
		shrt_weight= 1
		stdy_weight= 1

	pwr_val = 0
	rst_val = 0
	shrt_val= 0
	stdy_val= 0

	top_naps=[0,0,0,0] #best found power, resting, short, and study nap start times respectively

	for x in range(0, len(power_naps)):
		diff = abs(power_naps[x]-naptime)
		tmp_val = 100-(diff*diff)
		if tmp_val>pwr_val:
			pwr_val=tmp_val
			top_naps[0]=power_naps[x]

	for x in range(0, len(rest_naps)):
		diff = abs(rest_naps[x]-naptime)
		tmp_val = 100-(diff*diff)
		if tmp_val>rst_val:
			rst_val=tmp_val
			top_naps[1]=rest_naps[x]

	for x in range(0, len(short_naps)):
		diff = abs(short_naps[x]-naptime)
		tmp_val = 100-(diff*diff)
		if tmp_val>shrt_val:
			shrt_val=tmp_val
			top_naps[2]=short_naps[x]

	for x in range(0, len(study_naps)):
		diff = abs(study_naps[x]-naptime)
		tmp_val = 100-(diff*diff)
		if tmp_val>stdy_val:
			stdy_val=tmp_val
			top_naps[3]=study_naps[x]

	pwr_val *= pwr_weight
	rst_val *= rst_weight
	shrt_val*= shrt_weight
	stdy_val*= stdy_weight

	maxval=max(pwr_val, rst_val, shrt_val, stdy_val)

	# returns a 3-tuple containing (in order):
	# start time of best nap, duration of best nap, heuristic value of best nap

	if pwr_val==maxval:
		return [top_naps[0], 4, maxval]
	if rst_val==maxval:
		return [top_naps[1], 18, maxval]
	if shrt_val==maxval:
		return [top_naps[2], 9, maxval]
	if stdy_val==maxval:
		return [top_naps[3], 12, maxval]