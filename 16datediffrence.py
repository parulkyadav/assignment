def datecheck(d):
    
    if(d[1]>0 and d[1]<13):#to check month
        if(d[1]==2 or d[1]==4 or d[1]==6 or d[1]==9 or d[1]==11):
            datelast=30
        else:
            datelast=31
            
        if(d[2]>1900 and d[2]<3000): # to check year
            l=d[2]
            if(d[1]==2):
                if(d[2]%4==0):
                    if(d[2]%100==0):
                        if(d[2]%400==0):
                            #print("This is a leap year")
                            datelast=28
                    else:
                        #Print("This is a leap year")
                        datelast=28
                            
                            
            if(d[0]>0 and d[0] and d[0]<=datelast): #to check date
                return datelast
            else:
                print("Invalid date")
                
        
        else:
            print("Invalid year")
        
    else:
        print("Invalid month")
    
    
#date difference calculator


sdate=list(map(int,input("Enter the starting date").split('-')))
datelast=datecheck(sdate)
edate=list(map(int,input("Enter the ending date").split('-')))
if(edate[0]>sdate[0]):
    dd=edate[0]-sdate[0]
else:
    edate[0]+=datelast
    edate[1]-=1
    dd=edate[0]-sdate[0]
    
if(edate[1]>sdate[1]):
    md=edate[1]-sdate[1]
else:
    edate[1]+=12
    edate[2]-=1
    md=edate[1]-sdate[1]
    
yd=edate[2]-sdate[2]
print(dd,' days ',md,' months and ',yd,' years ')
