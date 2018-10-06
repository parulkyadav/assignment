num=int(input("Enter the digit to find its sum : "))
n=num
mul=1
while n:
    l=n%10
    mul*=l
    n=int(n/10)
print(mul)
