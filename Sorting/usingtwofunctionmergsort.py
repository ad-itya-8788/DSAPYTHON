def merg(left,right):
  result=[]
  i=j=0
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1
  while i<len(left):
    result.append(left[i])
    i+=1
  while j<len(right):
    result.append(right[j])
    j+=1
  return result


def mergsort(arr):
  if len(arr)<=1:
    return arr
  mid=len(arr)//2
  left=mergsort(arr[:mid])
  right=mergsort(arr[mid:])

  return merg(left,right)
arr=[44,33,2,1,34]
print("Array Before Sorting:",arr)
sorted=mergsort(arr)
print("Array After Sorting:",sorted)