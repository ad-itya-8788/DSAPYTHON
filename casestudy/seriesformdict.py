import pandas as pd
data={'a':10,'b':20,'c':30,'d':40}
print(data)

ser=pd.Series(data)

print(ser)

x=[1,2,3,4]
y=['A','B','C','D']
z=pd.Series(x,index=y)
print(z)

print(z.isin([1,2,30,4]))

sts = pd.Series(['apple','banana','cherry','date','elderberry'])

print(sts.str.startswith('b'))