import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpu as sns

penguins = sns.load_dataset("penguins")

print(penguins.head(8))

print("\n Missing Values in Each column :\n",penguins.isnull().sum())

penguins['bill_length_mm']=penguins['bill_length_mm'].fillna(penguins['bill_length_mm'].mean())

print("\n After filling missing bill length :\n",penguins.head(8))
