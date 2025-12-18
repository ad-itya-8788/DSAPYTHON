def search(arr,x):
  l=0
  r=len(arr)-1
  while l<=r:
    mid=(l+r)//2
    if arr[mid]==x:
      return mid
    elif x>arr[mid]:
      l=mid+1
    else:
      r=mid-1
  return 0

arr=[1,2,3,4,5]
found=search(arr,4)
if found==0:
  print("Element is Not Found")
else:
  print("Element is Found at index",found)