""" Case Study 1: NumPy Arrays & Universal Functions  
Problem: Using the car_crashes dataset, extract the speeding column as a NumPy 
array. 
• Compute the mean, median, and standard deviation. 
• Apply a universal function (e.g., np.sqrt) to transform values. 
• Compare speeding values against the national average (scalar). """

import numpy as np
import pandas as pd
import seaborn as sns

df=sns.load_dataset('car_crashes')

print("Mean of speeding:",np.mean(df['speeding']))
print("Median of speeing:",np.median(df['speeding']))
print("Standard Deviation of speeding:",np.std(df['speeding']))

print("Square Root of speediing:",np.sqrt(df['speeding']))

speed=df['speeding'].values
national_avg=10
comparison=speed>national_avg
print(comparison)