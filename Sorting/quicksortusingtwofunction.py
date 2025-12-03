def partiation(arr,pivot):
  lesser=[]
  grater=[]
  for x in arr:
    if x<=pivot:
      lesser.append(x)
    else:
      grater.append(x)
  return lesser,grater

def quicksort(arr):
  if len(arr)<=1:
    return arr
  pivot=arr[0]
  left,right=partiation(arr[1:],pivot)
  return quicksort(left)+[pivot]+quicksort(right)

arr=[44,33,2,1,34]
print("Array Before Sorting:",arr)
sort=quicksort(arr)
print("Array After Sorting:",sort)