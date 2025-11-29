import pandas as pd
import numpu as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
print("Dataset Loaded Successfully\n")

avg_flipper = penguins.groupby("species")["flipper_length_mm"].mean()
print("\nAverage Flipper Length:\n", avg_flipper)

rank_body_mass = penguins.groupby("species")["body_mass_g"].mean().sort_values(ascending=False)
print("\nSpecies Ranked by Body Mass:\n", rank_body_mass)

avg_flipper.plot(kind="bar",color=['orange','blue','green'])
plt.title("Average Flipper Length by Penguin Species")
plt.xlabel("Species")
plt.ylabel("Flipper Length (mm)")
plt.show()
