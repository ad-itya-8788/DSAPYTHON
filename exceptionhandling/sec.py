try:
  x=int(input("Enter a Number:"))
  res=x/10
except ZeroDivisionError:
  print("0 se divide nahi kr sakte app")
except ValueError:
  print("Sirf Value Enter Karo ")
else:
  print("Else tab chalta hai jab try mai kohi error na aayi ho:",res)

finally:
  print("Ye code hamesha run hota hai ye use hota hai jaise app ko database connection close krna hoga kohi resource close krna hoga")