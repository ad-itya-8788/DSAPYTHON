def sort(arr,pivot):
  left=[x for x in arr if x<=pivot]
  right=[x for x in arr if x>pivot]
  return left ,right

def quicksort(arr):
  if len(arr)<=1:
    return arr
  pivot=arr[0]
  left,right=sort(arr[1:],pivot)
  return quicksort(left)+[pivot]+quicksort(right)
arr=[4,3,2,1]
print(arr)
print("Sort:",quicksort(arr))