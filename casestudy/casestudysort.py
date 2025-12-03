""" Case Study 3: Ranking & Sorting with Pandas
Problem: Rank states by not_distracted crashes.
• Sort values in descending order.
• Display top 5 states.
• Assign ranks to each state."""

import numpy as np
import pandas as pd
import seaborn as sea

df=sea.load_dataset('car_crashes')

print(df)

sorted_df=df.sort_values(by="not_distracted" ,ascending=False)
print("Sorted:",sorted_df)

print("Top 5 States:",sorted_df.head(5))

df['rank']=df['not_distracted'].rank(ascending=False)
print("Data Frame With Ranks",df)