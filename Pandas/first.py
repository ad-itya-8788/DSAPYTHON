import pandas as pd

x=pd.Series([1,3,4,6,6,4,5,7,2,4,5,67,0,None])
print(x)

print("Indexing Values:")
print(x[2])

print("Slicing the Values(series):")
print(x[1:3])

print(x.index)


print(x.values)

print(x.dtype)

print(x.head(2))

print(x.tail())

print(x.sort_values())

print("Count Values:")
print(x.count())

print("Is Null:")
print(x.isnull())

print("Is Not Null:")
print(x.notnull)