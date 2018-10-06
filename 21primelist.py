def prime(x):
    flag=True
    for i in range(2,x):
        if(x%i==0):
            flag=False
            break
        else:
            flag=True
            
    if(flag):
        return 1
    else:
        return 0
        
l1=[]
n=int(input("Enter the last number of the prime series : "))
for i in range(n):
    if(prime(i)==1):
        l1.append(i)
for i in l1:
    print(i)
