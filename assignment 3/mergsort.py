def merg_sort(arr):
  if len(arr)<=1:
    return arr
  mid=len(arr)//2
  left=merg_sort(arr[:mid])
  right=merg_sort(arr[mid:])

  return sortar(left,right)

def sortar(left,right):
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

arr=[4,3,2,1,5,6,7]
print("Array Before sorting:",arr)
print("Array After Sorting:",merg_sort(arr))