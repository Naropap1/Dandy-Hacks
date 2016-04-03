# Test schedule!
#
# Busy from 9-12, 2-11
#
# Sleep from 12-4, 11-12
# -> WT = 5, BT = 23

import calc
from array import array

waketime = int(4*60/5)
bedtime = int(23*60/5)

wk1s = int(9*60/5)
wk1e = int(12*60/5)
wk2s = int(14*60/5)
wk2e = int(23*60/5)

occupied = [True] * 288

#print(occupied)
#print(len(occupied))

for x in range(wk1s,wk1e):
	occupied[x]=False
for y in range(wk2s,wk2e):
	occupied[x]=False

for i in range(0, waketime):
	occupied[x]=False
for j in range(bedtime, 288):
	occupied[x]=False

time_slept = (12-11)+(12-4)

#calc.set_sleeptimes(waketime, bedtime, time_slept)
#calc.set_occ(occupied)

calc.daily_naps(occupied, waketime, bedtime, time_slept, 0)