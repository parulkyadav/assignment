num=int(input("Enter the number : "))
n=num
add=0
while(n):
    l=n%10
    n=n//10
    add+=l*l
print(add)
