num=input("Enter the number to check armstrong : ")
numi=int(num)
n=int(num)
rev=0
for i in num:
    l=n%10
    rev=rev+(l*l*l)
    n=int(n/10)
print(rev)
if(rev==numi):
    print("armstrong number")
else:
    print("not a armstrong number")
