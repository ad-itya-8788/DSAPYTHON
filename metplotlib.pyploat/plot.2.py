import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('car_crashes')

plt.plot(df['speeding'], df['total'], 'r*-', label="Speed vs Driver")
plt.xlabel("Speeding")
plt.ylabel("Driver")
plt.legend()
plt.title("Speeding vs Car")
plt.grid()
plt.show()
