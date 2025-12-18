x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
try:
    res=x/y
except:
    print("Any Other Exception caught")
else:
    print(res)
finally:
    print("Thank You for using this code")