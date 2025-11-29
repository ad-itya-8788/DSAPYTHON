import pandas as pd
import numpy as np

# Create a Series
s = pd.Series(np.random.randint(1, 100, size=10))
print("Original Series:\n", s)

# ------------------------------
# BASIC FUNCTIONS
# ------------------------------
print("\nHead (Top 5):\n", s.head())
print("\nTail (Last 5):\n", s.tail())
print("\nData Type:", s.dtype)
print("Size:", s.size)
print("Index:", s.index)
print("Values:", s.values)

# ------------------------------
# STATISTICAL FUNCTIONS
# ------------------------------
print("\nSum:", s.sum())
print("Mean:", s.mean())
print("Median:", s.median())
print("Standard Deviation:", s.std())
print("Variance:", s.var())
print("Minimum:", s.min())
print("Maximum:", s.max())
print("Count:", s.count())
print("Describe Summary:\n", s.describe())

# ------------------------------
# INDEXING & SLICING
# ------------------------------
print("\nFirst Element:", s[0])
print("Slice (0 to 4):\n", s[0:5])
print("Using iloc (index 2):", s.iloc[2])
print("Using loc (index label 3):", s.loc[3])

# ------------------------------
# CHECKING FUNCTIONS
# ------------------------------
print("\nIs Null:\n", s.isnull())
print("Not Null:\n", s.notnull())
print("Unique Values:\n", s.unique())
print("Number of unique values:", s.nunique())
print("Value Counts:\n", s.value_counts())

# ------------------------------
# OPERATIONS (Scalar)
# ------------------------------
print("\nAdd 5 to each:", s + 5)
print("Multiply by 2:", s * 2)
print("Square of all values:\n", s ** 2)
print("Divide by 10:\n", s / 10)

# ------------------------------
# APPLY FUNCTION
# ------------------------------
print("\nSquare root of each:\n", s.apply(np.sqrt))

# ------------------------------
# SORTING
# ------------------------------
print("\nSort by Values:\n", s.sort_values())
print("Sort by Index:\n", s.sort_index())

# ------------------------------
# TYPE CONVERSION
# ------------------------------
print("\nConvert to Float:\n", s.astype(float))

# ------------------------------
# COPY & DROP
# ------------------------------
copy_s = s.copy()
print("\nCopy of Series:\n", copy_s)

# Drop a value at index 0
dropped_s = s.drop(0)
print("After dropping index 0:\n", dropped_s)
