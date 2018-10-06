num=int(input("Enter the digit to find its sum : "))
n=num
add=0
while n:
    l=n%10
    add+=l
    n=int(n/10)
print(add)
