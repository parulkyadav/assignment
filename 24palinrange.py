def palin(num):
    n=num
    rev=0
    while n:
        l=n%10
        rev=(rev*10)+l
        n=int(n/10)
    if(rev==num):
        return 1
    else:
        return 0

l1=[]
print("This is the program to print all four digit palindromes")
for i in range(1000,9999):
    if(palin(i)==1):
        l1.append(i)
print(*l1)
    
