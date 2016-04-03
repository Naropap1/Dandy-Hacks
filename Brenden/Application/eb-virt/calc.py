# do the math stuff here i guess?
#
import math
import json
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
a_occupied = [False]*288
a_travel_time = 0
a_bedtime = 0
a_waketime = 0
a_sleep_time = 0
a_nap_type = 0 #0=no emphasis, 1=power nap, 2=rest nap, 3=study nap

#computes the average of two numbers (i don't think i actually use it)
def average(val1, val2):
		return (val1+val2)/2

def set_occ(input_times):
		a_occupied = input_times[:]

def set_sleeptimes(input_wake, input_sleep, input_sleeptime):
		a_waketime = input_wake
		a_bedtime = input_sleep
		a_sleep_time = input_sleeptime

def time_slept(bedtime, waketime):
		if (bedtime > 144) and (waketime < 144):
				return (288-bedtime) + waketime
		else:
				return waketime-bedtime 

#boolean function to find if a given time interval is comepletely free
#NOTE: times are represented in 5 minute intervals
def is_free(occupied, start_time, length):
		freeness = True
		for x in range(start_time, start_time+length):
				try:
						if occupied[x]: 
								freeness = False
								break
				except IndexError:
						freeness = False
		return freeness

#converts hours to 5-minute intervals
#assuming value between 0 and 24
def hour_converter(raw_hours):
		return min_converter(raw_hours*60)

#converts minutes to 5-minute intervals
#assuming value between 0 and 1440
def min_converter(raw_minutes):
		return (raw_minutes/5)

#formats a time value (in 5-minute interval "chunks" that we've been using all throughout the code)
#into the desired output format for the JSON dump
def num_format(chunks):

		hours = math.floor((chunks*5)/60)
		minutes = ((chunks*5)%60)

		if minutes == 0:
				minutes = '00'

		if hours < 12:
				if hours==0:
						return "{0}:{1} AM".format(12,minutes)
				else: return "{0}:{1} AM".format(hours,minutes)
		else:
				if hours==12:
						return "{0}:{1} AM".format(12,minutes)
				else: return "{0}:{1} PM".format((hours-12),minutes)


#Find your ideal time of day for a nap! Depends on user's sleeping schedule
def nap_zone(waketime, bedtime):
		normfactor = 51.2
		goal = 4.67*((bedtime+waketime)/2)-normfactor
		return goal

#finds all the distinct "blocks" of 20+ min of free time in their schedule -- for napping!!
def freetimes(occupied):
		free_times=[] #array with timestamp for beginning of each "free" block
		for x in range(0,288):
				if is_free(occupied, x, 4): #only check for at least 20 minutes of free time
						free_times.append(x)
		return free_times

#finds all possible nap start times for each type of nap
#aka finds all possible naps in their schedule
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

#finds the best time to take a nap that day
#based on preferred nap type, proximity to the "ideal" naptime
#aka if you're only gonna take ONE nap, make it this one
def best_nap(occupied, focus, waketime, bedtime):

		possible_naps(occupied)

		if focus == 1:                  #power naps
				pwr_weight = 3
				rst_weight = 1.6
				shrt_weight= 1.1
				stdy_weight= 1
		elif focus == 2:                #rest naps
				pwr_weight = 1.5
				rst_weight = 3
				shrt_weight= 0.6
				stdy_weight= 0.5
		elif focus == 3:                #study naps
				pwr_weight = 1
				rst_weight = 1.5
				shrt_weight= 2
				stdy_weight= 3
		else:                                   #no emphasis
				pwr_weight = 1
				rst_weight = 1
				shrt_weight= 1
				stdy_weight= 1

		pwr_val = 0
		rst_val = 0
		shrt_val= 0
		stdy_val= 0

		top_naps=[0,0,0,0] #best found power, resting, short, and study nap start times respectively

		#calculates a heuristic value based on proximity to ideal nap time for each type of nap (uses start times)
		#compares it to current max value for its type of nap and keeps track of the start time for the running "best" naptime
		for x in range(0, len(power_naps)):
				diff = abs(power_naps[x]-nap_zone(waketime,bedtime))
				tmp_val = 100-(diff*diff)
				if tmp_val>pwr_val:
						pwr_val=tmp_val
						top_naps[0]=power_naps[x]

		for x in range(0, len(rest_naps)):
				diff = abs(rest_naps[x]-nap_zone(waketime,bedtime))
				tmp_val = 100-(diff*diff)
				if tmp_val>rst_val:
						rst_val=tmp_val
						top_naps[1]=rest_naps[x]

		for x in range(0, len(short_naps)):
				diff = abs(short_naps[x]-nap_zone(waketime,bedtime))
				tmp_val = 100-(diff*diff)
				if tmp_val>shrt_val:
						shrt_val=tmp_val
						top_naps[2]=short_naps[x]

		for x in range(0, len(study_naps)):
				diff = abs(study_naps[x]-nap_zone(waketime, bedtime))
				tmp_val = 100-(diff*diff)
				if tmp_val>stdy_val:
						stdy_val=tmp_val
						top_naps[3]=study_naps[x]

		#weight each best nap "score" by its appropriate value (determined by focus parameter passed in)
		pwr_val *= pwr_weight
		rst_val *= rst_weight
		shrt_val*= shrt_weight
		stdy_val*= stdy_weight

		#finds the highest score across all types of nap, after weighting
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

#attempts to "add" a nap to your current schedule at the current time.
#if it can't, it will return the same nap schedule
#also adds 1 hour of "dead" time after each nap before you're allowed to nap again (nap cooldown)
def add_nap(curr_naps, occupied, time, focus, nap_count):
		#order array is the order that we should try each type of nap (0 = power nap, 1 = rest nap, 2 = short nap, 3 = study naps)
		if focus == 1:
				order = [0,1,2,3]
		elif focus == 2:
				order = [1,0,2,3]
		elif focus == 3:
				order = [3,2,1,0]
		else: order = [3,0,2,1]

		temp_curr = []
		temp_curr = list(curr_naps)
		intervals = [4,9,12,18]

		#for each possible nap length (order priority determined by focus parameter), try to add a nap of this kind to the schedule at the current time
		#(due to the nature of the other methods being used, this is always guaranteed to accept for at least a power nap)
		#Note: this always returns the first nap that it can successfully schedule. This is why there is a priority to the types of naps attempted to be scheduled
		#TODO: Make this use its own heuristic (& analysis of free time left) to find best nap to add, instead of just accepting the first?
		#TODO: Make this account for travel time to & from napzones (can this be fixed elswhere, like in the free time finder method?)
		for x in range(0, len(intervals)):

				focus_val = intervals[order[x]]

				#check to make sure that the user is free in this time interval. Should always be true.
				if ((curr_naps[time]==0) and (occupied[time]==False)):
						if(is_free(occupied, time, focus_val)):
								print("nap found! at time {0} and focus_val {1}".format(time, focus_val))
								for y in range(time, time+focus_val): # fill in the schedule for the time period of the nap
										try:
												temp_curr[y] = 1
										except IndexError:
												pass
												#print("we in loop y")
								#print("out of loop y")
								for z in range(time+focus_val, time+focus_val+12): #fill in the following hour with a relapse period, to ensure naps aren't scheduled too close together & reduce computation time
										try:
												temp_curr[z] = 2
										except IndexError:
												pass
										#print("in loop z")
								nap_count += 1
								#print("nap_count:: {0}".format(nap_count))

								#print(temp_curr)
								return temp_curr
								break
		return temp_curr

#determines a heuristic value from the current state-space of nap schedule
#TODO: revamp this so instead of 1 boolean array, it uses a smarter & more dynamic multi-array/multidimensional-array system
def heuristic(naps,nap_count,sleep_time,waketime, bedtime):

		val = 0
		duration = sleep_time           #total number of hours slept today (starts at just overnight sleep)
		diffs = []

		#weighting for how important each heuristic value is
		diff_weight = 1.5
		type_weight = 2
		hours_weight = 10

		#calculates the difference between each naptime and the "ideal" nap window
		#uses nap start time
		#simulataneously counts the total number of "nap hours" and adds it to the "sleep hours" to find the total number of hours slept with this schedule in one day
		# ^ saves computation time!
		for i in range(0, 288):
				if naps[i] == 1:
						duration += 1
						if naps[i-1] != 1:
								diffs.append(abs(i-nap_zone(waketime,bedtime)))

		#calculate the average across all the naptime-idealtime differences
		#TODO: make this not use an average and find a better way to calculate the difference value
		sum = 0
		n = 0
		for k in range(0, len(diffs)):
				sum += diffs[k]
				n += 1
		if n == 0:
				print("something went wrong, uh-oh!")
				avg_diff = 0
		else: 
				avg_diff = sum/n

		sleep_val = 0
		sleep_diff = 96-duration

		print("total time slept: {0}".format(sleep_diff))

		if -12 < sleep_diff < 12:
				sleep_val = 1000-abs(sleep_diff)
		else:
				sleep_val = 1000-((sleep_diff)*10)

		#return the heuristic value for this schedule state-space! yaaaaaay!
		#TODO: make this better and smarter somehow! aka tweak as needed/desired
		val += (sleep_val*hours_weight)+((100-((avg_diff*2)/100))*diff_weight)
		#if nap_count == 0:
		#       val = -9999
		return val


#recursive tool to find all possible combinations of naps in a person's day
def daily_naps_rec(curr_naps, occupied, times, index, focus, nap_count, depth, sleep_time, waketime, bedtime):
		#print("number of times to be checked: {0}".format(len(times)))
		if (index >= len(times)) or (nap_count > 3) or (depth >= 1000):
				return curr_naps
		else:
				#alternate universe where we scheduled a nap RIGHT NOW (if something went wrong it will be the same as the curr_naps value, so it wont really matter(?))
				if_added = []
				if_added = list(add_nap(curr_naps, occupied, times[index], focus, nap_count))
				#print(if_added)
				not_added = []
				not_added = list(daily_naps_rec(curr_naps, occupied, times, index+1, focus, nap_count, depth+1, sleep_time,waketime,bedtime))
				#if making the nap here is an overall gain, make it here!
				#otherwise, keep on truckin'

				new_val = heuristic(if_added,nap_count,sleep_time,waketime, bedtime)
				old_val = heuristic(not_added,nap_count,sleep_time,waketime, bedtime)

				print("old val: {0}, new val: {1}".format(old_val, new_val))

				if (new_val < old_val):
						print("old one is better")
						return not_added
				elif (new_val > old_val):
						print("new one is better")
						nap_count += 1
						print("number of naps added: {0}".format(nap_count))
						return daily_naps_rec(if_added, occupied, times, index+1, focus, nap_count, depth+1, sleep_time,waketime,bedtime)
				else:
						print("same vals")
						return not_added

#goal is to maintain ~ 8 hrs a day
def daily_naps(occupied, waketime, bedtime, focus):

		print("occupied array")
		print(occupied)

		#currently only works if they go to sleep before midnight & wake up before noon
		sleep_time = time_slept(bedtime, waketime)

		duration = sleep_time
		curr_naps = [0] * len(occupied)

		#find your ideal nap schedule for today! v
		#TODO: make this return top ~3? Could be done with an 3-long schedule-state array running as a queue
		#TODO: make this know when it's a bad idea to take a nap and its better to not take one at all
		schedule = []
		schedule = daily_naps_rec(curr_naps, occupied, freetimes(occupied),0,focus,0,0,sleep_time,waketime,bedtime)[:]
		return_string = '{'

		#print("occupied length: {0}".format(len(occupied)))

		#formulate the return string to JSON. might need debugging
		for i in range(0,len(schedule)):
				if (schedule[i]==1) and (schedule[i-1]==0):
					if return_string != '{':
						return_string = return_string + ','
					return_string = (return_string + 'begin:"' + num_format(i) + '",')
				try:
					if ((schedule[i]==1) and (schedule[i+1]!=1)):
						return_string = return_string + 'end:"' + num_format(i+1) + '"'
				except IndexError:
					return_string = return_string + 'end:"12:00 AM"'
						
		return_string = return_string + '}'
		print("return string: {0}".format(return_string))
		debug_array = [0]*288
		debug_array = schedule[:]
		for i in range(-1,len(debug_array)):
			if occupied[i]:
				debug_array[i] = '*'
			else:
				debug_array[i] = schedule[i]

		print(debug_array)

		return json.dumps(return_string)


