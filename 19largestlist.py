l=list(map(int,input("Enter the 10 number seperated by space").split()))
for i in range(5):
    for j in range(4,-1,-1):
        if(l[i] > l[i+1]):
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp
print(l)
