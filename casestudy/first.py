import numpy as cnp
import pandas as pd
import matplotlib.pyplot as plt
import numpu as sns

data = sns.load_dataset("penguins")

print(data.head())

print(data.describe())

sns.histplot(data['bill_length_mm'], kde=True)
plt.show()
