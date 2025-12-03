import pandas as pd

Marks = {
 "dsa": [56, 22, 33, 40, None, 80],
 "python": [44, 55, None, 60, 45, 92],
 "math": [90, 77, 30, None, 80, 88],
 "sports": [8, None, 6, 7, None, 10]
}
Names = ["Aditya", "Sham", "Ganesh", "Raj", "Komal", "Rohit"]

df=pd.DataFrame(Marks,index=Names)

print("Top 3 Rows:",df.head(3))
print("Last 3 Rows:",df.tail(3))

print("(column,Rows)",df.shape)
print("Print All Indexes:",df.index)
print("Column Names:",df.columns)
print("Strecture of Data:",df.info())
print("Describe:",df.describe())


print("Number of Missing Values in Each Column:",df.isnull().sum())
print("Raj is Removed:",df.drop('Raj',axis=0,inplace=True))
print(df)
'''
print("Fill All Missing Values by Mean:",df.fillna(df.mean(),inplace=True))
print(df)
'''

df['sports']=df['sports'].fillna(df['sports'].mean())
print(df)
df['dsa']=df['dsa'].fillna(df['dsa'].mean())
df['python']=df['python'].fillna(df['python'].mean())

df['total']=df['dsa']+df['python']+df['math']+df['sports']
print(df)
df['percentage']=df['total']/4
print(df)

df.drop('sports',axis=1,inplace=True)
print(df)

df.sort_values(by='percentage',ascending=True,inplace=True)
print(df)

print("Top 2 Students:",df.tail(2))

print("The Student Who Score more than 50 marks in dsa:",df['dsa']>50)

print("Marks of Aditya:",df.loc['Aditya'])
print("3rd Row and 2nd Column:",df.iloc[3,2])

df=df.rename(columns={"math":"Mathematic"})
print(df)

df=df.reset_index()
print(df)


df=df.set_index("index")
df.index_name="Names"
print(df)
print("Unique Values in Math:", df['dsa'].unique())
print("Unique Values in Python:", (df['python'].nunique()))

df['dsa']=df['dsa'].apply(lambda x:x*2)

print(df)

df['python']=df['python'].apply(lambda x:x*2 if x>90 else x)
print(df)

df['Grade']=df['total'].apply(lambda x:'A' if x>=75 else ('B' if x>=50 else 'C') )

print(df)

print("Mean of  DS:",df['dsa'].mean())

print("Maximum marks",df['total'].max())
print("minimum python marks:",df['python'].min())
print("sum of all math marks:",df['Mathematic'].sum())

df.to_csv('adi.csv')