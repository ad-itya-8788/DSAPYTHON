fp=open("adi.txt")
while True:
  k=fp.readline()
  if k=="":
    break
  print(k,end=" ")
