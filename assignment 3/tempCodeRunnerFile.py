def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a

x=int(input("Enter First Number:"))
y=int(input("Enter second Number:"))
print("Gcd is:",gcd(x,y))