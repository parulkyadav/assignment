def palin(num):
    n=num
    rev=0
    while n:
        l=n%10
        rev=(rev*10)+l
        n=int(n/10)
    if(rev==num):
        print("Plaindrome")
    else:
        print("Not Plaindrome")
        
palin(int(input("Enter the number to find it is palindrome or not : ")))

