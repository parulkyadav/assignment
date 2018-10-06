def feb(n):
    a=0
    b=1
    flag=0
    for i in range(1000):
        temp=a
        a=b
        b=b+temp
        if(b==n):
            return(True)

    
r=feb(int(input("Enter the number to be searched for fabonnacci : ")))
if r:
    print("This is a fabonnacci number")
else:
    print("This is not a fabonnacci number")

    
