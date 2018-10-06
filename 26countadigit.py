num=int(input("Enter the number : "))
d=int(input("Enter the digit to be counted : "))
n=num
count=0
while(n):
    l=n%10
    n=n//10
    if(l==d):
        count+=1
print(count)
