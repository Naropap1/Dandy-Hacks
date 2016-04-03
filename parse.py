
minutesOccupied = [0]* len(times)
occupied = [False]*288

def innerHelperLoop(x):
     for y in range(5):
        for z in range(0,len(minutesOccupied),2):
            if x*5+y >= minutesOccupied[z]:
                if x*5+y <= minutesOccupied[z+1]:
                    occupied[x]=True;
                    return
               
def findOccupied(times):
     #parse
     index=0
     temp=0
     for x in times:
         x=x.replace(':',' ')
         x=x.split(' ')
         temp=temp+int(x[1])
         if x[2]=='AM':
             if int(int(x[0]))<12:
                 temp=temp+int(x[0])*60
         else:
             if int(int(x[0]))<12:
                 temp=temp+ int(x[0])*60+12*60
             else:
                 temp=temp+ 12*60
         minutesOccupied[index]=temp
         index=index+1
         temp=0
     #print(minutesOccupied)

     for x in range(288):
         innerHelperLoop(x)

     return occupied
        


