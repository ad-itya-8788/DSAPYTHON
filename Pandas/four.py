import pandas as pd
data=pd.DataFrame({'Name':['Aditya','Sham'],'Age':[21,23]})
print(data)


x=pd.Series([1,2,3,4,5])
y=pd.Series([11,22,33,44,55])
z=pd.DataFrame({'c':x,'c2':y})
print("DataFrame By series")
print(z)