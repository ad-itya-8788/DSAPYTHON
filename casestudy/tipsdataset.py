""" Using the tips dataset from Seaborn, perform the following data analysis tasks:

Apply the log transformation on the total_bill column and display the transformed values.

Normalize the tip column using the formula:

normalized_tip
=
tip
−
mean(tip)
std(tip)
normalized_tip=
std(tip)
tip−mean(tip)
	​


Count and display how many customers gave a tip greater than 5 by performing a scalar comparison.

Compute the tip percentage for each entry using the formula:

tip_percentage
=
tip
total_bill
×
100
tip_percentage=
total_bill
tip
	​

×100

and print the resulting column."""

import pandas as pd
import numpy as np
import seaborn as sns

df=sns.load_dataset('tips')

total_bill=df['total_bill']

#print(total_bill)

print("Log Value applay to totla bill",np.log(total_bill))

nortip=df['tip']-np.mean(df['tip'])/np.std(df['tip'])
print("Normalize the tip:",nortip)

print("Count How many customer give more than 5 top:",df['tip']>5)

tip_percentage=df['tip']/df['total_bill']*100
print("Tip Percentage",tip_percentage)