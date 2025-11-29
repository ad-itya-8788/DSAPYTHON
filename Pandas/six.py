import pandas as pd
x=pd.DataFrame({'a':[1,2,3,4,5],'b':[11,22,33,44,55]})
print(x)

print("Values is Only Grater than 2 from column a")

print("Index Values ")
print(x[x['a']>2]['a'])

x['tips']=[111,222,333,444,555]

print(x)

print("After Deleting tips column")
x=x.drop(columns=['tips'])
print(x)