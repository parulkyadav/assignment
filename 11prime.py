def prime(x):
    flag=True
    for i in range(2,x):
        if(x%i==0):
            flag=False
            break
        else:
            flag=True
            
    if(flag):
        print("Prime")
    else:
        print("Not prime")
        
prime(int(input("Enter a number to find its prime : ")))        
