n=int(input("Enter the number : "))
cube=[]
for i in range(1,n):
    if(i%3==0):
        cube.append(i*i*i)
for i in cube:
    print(i)
