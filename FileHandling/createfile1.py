x=input("enter name:")
try:
  fp=open("adi.txt","a")
  fp.write(x)
except Exception as e:
  print(e)