import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=sns.load_dataset('car_crashes')

alc=df['alcohol']
spd=df['speeding']

plt.scatter(alc,spd)
plt.show()

plt.hist(df['total'],bins=10,color='skyblue')
plt.show()