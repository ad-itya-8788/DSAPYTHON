import pandas as pd
x=pd.Series((1,22,0,None))

x.fillna(3)

print(x)