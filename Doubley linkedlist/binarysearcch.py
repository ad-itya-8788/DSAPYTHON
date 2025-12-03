def binarysearch(arr,x):
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
  return -1
arr=[1,2,3,4,5,6,7,8]
print("Element 5 found at index:",binarysearch(arr,5))