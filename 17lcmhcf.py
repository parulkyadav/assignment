num=int(input("Enter a value : "))
l1=[]
while num:
    for i in range(2,num):
        if num%i == 0 :
            l1.append(i)
            num=int(num/i)
            print(num)
            print(l1)
        i-=1
