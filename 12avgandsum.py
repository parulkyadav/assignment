num=int(input("Enter the value : "))
l1=list(map(int,input("Enter 10 postive integers seperated by space : ").split()))
print(l1)
add=0
count=0
for i in l1:
    add+=i
    count+=1
avg=add/count   
print("Total is : {} \nAverage is : {}  ".format(add,avg))
