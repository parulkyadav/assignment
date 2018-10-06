x=int(input("Enter the first digit : "))
y=int(input("Enter the second digit : "))
print("+ , - , / , * , %")
o=input("Enter the operator : ")
if(o=="+"):
    print("\n",x,' + ',y,' = ',x+y)
elif(o=="-"):
    print("\n",x,' - ',y,' = ',x-y)
elif(o=="/"):
    print("\n",x,' / ',y,' = ',x/y)
elif(o=="*"):
    print("\n",x,' * ',y,' = ',x*y)
elif(o=="%"):
    print("\n",x,' % ',y,' = ',x%y)
else:
    print("Invalid input")
    
