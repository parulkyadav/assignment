num=int(input("Enter the number to be reversed : "))
n=num
rev=0
while n:
    l=n%10
    rev=(rev*10)+l
    n=int(n/10)
print("The reversed number is : ",rev)
print("The double of reversed number is : ",rev*2)
