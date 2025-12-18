class Age(Exception):
  def __init__(self,msg):
    super().__init__(msg)
    self.msg=msg
age=int(input("Enter age:"))
try:
  if age<18:
   raise Age("Are Bhai Age chota hai")
except e:
  print("Error hai :",e.message)
else:
  print("Age hai",age)