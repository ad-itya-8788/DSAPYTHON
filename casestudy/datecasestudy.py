import pandas as pd
dt=pd.date_range(start="2026-01-01",end="2026-01-20",freq="D")
print(dt[:5])
print(dt[-5:])

print("Total Dates:",len(dt))

df=pd.DataFrame(dt,columns=['Date'])
print(df)
df['Date_time_format']=pd.to_datetime(df['Date'])
df['Day']=df['Date'].dt.day
df['Month']=df['Date'].dt.month
df['Year']=df['Date'].dt.year

print(df)

df['WeekDay']=df['Date'].dt.weekday
print(df)

df['Is_weekEnd']=df['WeekDay'].isin([5,6])

print(df)
weekends=df[df['Is_weekEnd']==True]
print(df)

print(weekends)

df['prev_day']=df['Date']-pd.Timedelta(days=1)
df['Next_Day']=df['Date']+pd.Timedelta(days=1)
print("Result of Date:",df)

# Q5: 10 hourly timestamps
hourly = pd.date_range(start="2026-01-01 00:00", periods=10, freq="H")

df2 = pd.DataFrame(hourly, columns=['Date'])

# Create FutureDate = Date + (2 weeks + 3 days + 12 hours)
df2['FutureDate'] = df2['Date'] + pd.Timedelta(weeks=2, days=3, hours=12)

print("\nQ5 Result:")
print(df2)

# Extract hour
df2['Hour'] = df2['Date'].dt.hour

# Filter hour > 12
filtered = df2[df2['Hour'] > 12]

print("\nQ6 Result (Hour > 12):")
print(filtered)
