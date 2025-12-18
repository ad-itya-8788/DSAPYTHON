def quick_sort(arr):
  if len(arr)<=1:
    return arr
  pivot=arr[0]
  lesser=[x for x in arr[1:] if x<=pivot]
  grater=[x for x in arr[1:] if x>pivot]
  return quick_sort(lesser)+[pivot]+quick_sort(grater)
arr=[5,4,3,2,1,4,5]
print("Before Sorting:",arr)
print("After Sorting:",quick_sort(arr))