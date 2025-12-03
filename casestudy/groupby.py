import pandas as pd
import numpy as np
import seaborn as sea

df=sea.load_dataset('tips')

z = df.groupby('sex')[['total_bill', 'tip']].sum()
print(z)


