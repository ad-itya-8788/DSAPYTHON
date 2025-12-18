class DivideByZeroError(Exception):
  def __init__(self,msg):
    super().__init__(msg)
    self.msg=msg
x=int(input("Enter first number:"))
y=int(input("Enter Second Number:"))
try:
  if y==0:
     raise DivideByZeroError("You Cant divide By zero")
  z=x//y
except ValueError:
  print("Enter Values Only")
except DivideByZeroError as e:
  print(e)
else:
  print("result is:",z)
finally:
  print("calculation attemnpt is Finished")