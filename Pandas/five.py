import pandas as pd
data=pd.DataFrame({'Name':['Aditya','Sham'],'Age':[21,23]})
print(data)


x=pd.Series([1,2,3,4,5])
y=pd.Series([11,22,33,44,55])
z=pd.DataFrame({'c':x,'c2':y})
print("DataFrame By series")
print(z)

print(z.shape)
print("Columns")
print(z.columns)
print(z.loc[1,'c'])
print(z.iloc[1,1])


print(z.head())
print(z.tail())


print("info",z.info())

print(z.describe())

