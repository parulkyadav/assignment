num=int(input("Enter the value : "))
n=num
r=0
res=0
while(n):
    l=n%10
    r+=l
    n=int(n/10)
while(r):
    last=r%10
    res+=last
    r=int(r/10)
print(res)
