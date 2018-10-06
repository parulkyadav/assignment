def vowelcon(val):
    l1=['a','e','i','o','u','A','E','I','O','U']
    flag=True
    for i in l1:
        if(i==val):
            flag=False
            break
        else:
            flag=True
    if flag:
        print(val," is a consonent")
    else:
        print(val," is a vowel")
         
vowelcon(input("Enter a character : "))

