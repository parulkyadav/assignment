"""series:1,2,4,7,11,16,22,29,37......"""
n=int(input("Enter the number of series for the series : "))
i=1
res=1
l1=[1]
while(i<n):
    j=1
    while(j<=i):
        res+=1
        j+=1
    l1.append(res)
    i+=1
print(l1)
