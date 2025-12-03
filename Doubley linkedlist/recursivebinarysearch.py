def search(arr,l,r,x):
  if l>r:
    return -1
  mid=(l+r)//2
  if x==arr[mid]:
    return mid
  elif x<arr[mid]:
    return search(arr,l,mid-1,x)
  else:
    return search(arr,mid+1,r,x)

arr=[1,2,3,4,5]
print("Element Found at index:",search(arr,0,len(arr)-1,5))