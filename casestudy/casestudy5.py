import pandas as pd
marks={"DSA":[56,7,84,32],"C++":[34,56,33,22],"Java":[56,44,33,22],"Python":[44,33,None,11]}
print(marks)


student=["Aditya","Sham","Ganesh","Raj"]

df=pd.DataFrame(marks,index=student)
print(df)

df.loc['Sham','DSA']=None
print(df)


print("After Filling Marks By Mean:")
df.fillna(df.count(),inplace=True)
print(df)