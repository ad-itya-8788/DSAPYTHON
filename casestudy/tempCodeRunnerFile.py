import pandas as pd
dt=pd.date_range(start="2026-01-01",end="2026-01-20",freq="D")
print(dt[:5])
print(dt[-5:])

print("Total Dates:",len(dt))

df=pd.DataFrame(dt)
print(df)
df['Date_time_format']=pd.to_datetime(df['dt'])
df['Day']=df['df'].dt.day
df['Month']=df['df'].dt.Month
df['Year']=df['df'].dt.Year