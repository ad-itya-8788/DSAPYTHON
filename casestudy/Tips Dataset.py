'''Using the tips dataset from Seaborn, perform the following tasks:

Compute the mean, median, and standard deviation of the total_bill column.

Apply a NumPy universal function (such as np.square()) to transform the values of the total_bill column.

Compare each total_bill value with a given national average (use 20 as the benchmark) and display whether each value is greater than the average (True/False).'''

import numpy as np
import seaborn as sns

df=sns.load_dataset("tips")
total_bill=df['total_bill']
print(df)
print("Mean of total Bill:",np.mean(total_bill))
print("Median of total Bill",np.median(total_bill))
print("Standard Deviation:",np.std(total_bill))

print("Applay Sepal_width:",np.square(df['total_bill']))

national_av=89
comp=total_bill>national_av
print("Is total Bill Grater than Nationla Avg:")
print(comp)