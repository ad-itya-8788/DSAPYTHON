def quicksort(list1):
  if len(list1)<=1:
    return list1
  else:
    pivot=list1[0]
    lesser=[x for x in list1[1:] if x<=pivot]
    grater=[x for x in list1[1:] if x>pivot]
    return quicksort(lesser)+[pivot]+quicksort(grater)

list1=[11,22,1,2,3,15]
sortlist=quicksort(list1)
print(sortlist)