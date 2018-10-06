n=int(input"Enter the number of terms for fabonnacci : ")
l1=[0,1]
a=0
b=1
for i in range(10):
    temp=a
    a=b
    b=b+temp
    l1.append(b)

for i in l1:
    print(i)
