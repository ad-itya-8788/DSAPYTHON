class Age(Exception):
  def __init__(self,msg):
    super().__init__(msg)
    self.msg=msg
age=int(input("Enter age:"))
try:
  if age<18:
   raise Age("Are Bhai Age chota hai")
except Age as e:
  print("Error hai :",e)
else:
  print("Age hai",age)