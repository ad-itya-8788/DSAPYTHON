import pandas as pd
marks={"dsa":[11,22,33],"python":[44,55,22],"math":[56,77,30]}
name=["Aditya","Sham","Ram"]

df=pd.DataFrame(marks,index=name)
print(df)
df.drop('Aditya',axis=0,inplace=True)
print(df)

df.drop('math',axis=1,inplace=True)
print(df)