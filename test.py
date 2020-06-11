# Test schedule!
#
# Busy from 9-12, 2-11
#
# Sleep from 12-4, 11-12
# -> WT = 5, BT = 23

import calc
from array import array

waketime = int(5*60/5) #5 AM
bedtime = int(23*60/5) #11 PM

wk1s = int(10*60/5)
wk1e = int(14*60/5)
wk2s = int(17*60/5)
wk2e = int(21*60/5)

occupied = [False] * 288


for x in range(wk1s,wk1e):
	occupied[x]=True
#for y in range(wk2s,wk2e):
#	occupied[y]=True

for i in range(0, waketime):
	occupied[i]=True
for j in range(bedtime, 288):
	occupied[j]=True


calc.daily_naps(occupied, waketime, bedtime, 0)