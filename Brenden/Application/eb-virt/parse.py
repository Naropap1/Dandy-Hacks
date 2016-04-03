
minutesOccupied = [0]
occupied = [False]*288

def calcMinutes(string):
     temp=0
     string=string.replace(':',' ')
     string=string.split(' ')
     temp=temp+int(string[1])
     if string[2]=='AM':
          if int(int(string[0]))<12:
               temp=temp+int(string[0])*60
     else:
          if int(int(string[0]))<12:
               temp=temp+ int(string[0])*60+12*60
          else:
               temp=temp+ 12*60
     return temp

def innerHelperLoop(x,times):
     for y in range(5):
        for z in range(0,len(minutesOccupied)-1,2):
            if x*5+y >= minutesOccupied[z]:
                if x*5+y <= minutesOccupied[z+1]:
                    occupied[x]=True;
                    return

def findOccupied(times):
     minutesOccupied = [0]*len(times)
     #parse
     index=0
     for x in times:
         minutesOccupied[index]= calcMinutes(x)
         index=index+1
     #print(minutesOccupied)

     for x in range(288):
         innerHelperLoop(x,times)

     return occupied
        


