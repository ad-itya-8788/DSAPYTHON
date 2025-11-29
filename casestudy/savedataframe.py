import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(5), index=np.arange(5))
print(df)

print(df.columns)

x = df.to_numpy()
print(x)

# Correct second dataframe
xn = pd.DataFrame([1,2,3,4], index=[5,6,7,8])
print(xn)

print(df.describe())
print("Mean :", df.mean())

print("loc:", df.loc[0, 0])
