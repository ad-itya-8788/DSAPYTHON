import numpy as np
import pandas as pd
import seaborn as sea

df=sea.load_dataset('tips')

z=df.groupby('sex').agg({'total_bill':'sum','tip':'sum'})
print(z)