def toh(n,start,helper,end):
  if n==1:
    print("Move Disk form",start,"to",end)
    return
  toh(n-1,start,end,helper)
  print("Move Disk",n,"  form",start,"to",end)
  toh(n-1,helper,start,end)


n=3
toh(n,"A","B","C")