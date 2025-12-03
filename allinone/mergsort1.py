def mergsort(arr):
  if len(arr)<=1:
    return arr
  mid=len(arr)//2
  left=arr[:mid]
  right=arr[mid:]
  mergsort(left)
  mergsort(right)
  i=j=k=0
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      arr[k]=left[i]
      i+=1
    else:
      arr[k]=right[j]
      j+=1
    k+=1
  while i<len(left):
    arr[k]=left[i]
    i+=1
    k+=1
  while j<len(right):
    arr[k]=arr[j]
    k+=1
    j+=1
  return arr
arr=[5,4,3,2,1]
print(arr)
print("Array After Sorting:",mergsort(arr))