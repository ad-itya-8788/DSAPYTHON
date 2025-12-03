import pandas as pd

print("print Date")

date_range=pd.date_range(start='2026-01-01',end='2027-01-10',freq='YE')
print(date_range)


data={'Date':['2016-01-01','2026-02-10','2026-03-20']}
df=pd.DataFrame(data)
df['Date']=pd.to_datetime(df['Date'])ku