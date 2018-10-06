def counting(num):
    n=num
    count=0
    if n==0 :
        print(1)
    else:
        while n:
            l=n%10
            n=int(n/10)
            count+=1
        print(count)
        
counting(int(input("Enter a number : ")))

