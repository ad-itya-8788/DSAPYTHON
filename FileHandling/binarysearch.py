def search(arr,x):
    l=0
    h=len(arr)-1
    while l<h:
        m=(l+h)/2
        if arr[m]==x:
            return m
        elif arr[m]<x:
            l=m+1
        else:
            h=m+1
    return -1
arr=[1,2,3,4,5]
x=3
res=search(arr,x)
if(res==-1):
    print("Not Found")
else:
    print("Found")