
# Assignment No. 5
# Demonstration of Basic Python Libraries

# Import Libraries
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 1. Math Library
print("Math Library:")
print("Square Root of 25:", math.sqrt(25))
print("Factorial of 5:", math.factorial(5))
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.8:", math.floor(4.8))
print()

# 2. NumPy Library
print("NumPy Library:")
data = np.array([50, 55, 60, 65, 70, 80])

print("Array:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", round(np.std(data), 4))
print()

# 3. SciPy Library
print("SciPy Library:")
study_hours = np.array([1, 2, 2, 3, 4, 5])

mode_result = stats.mode(study_hours, keepdims=False)
correlation = stats.pearsonr(study_hours, data)

print("Mode of Study Hours:", mode_result.mode)
print("Correlation:", round(correlation.statistic, 4))
print()

# 4. Pandas Library
print("Pandas Library:")

df = pd.DataFrame({
    "Study_Hours": study_hours,
    "Marks": data
})

print("Dataset:")
print(df)

print("\nFirst Five Records:")
print(df.head())

print("\nNull Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())
print()

# 5. Matplotlib Library
print("Matplotlib Visualization:")

plt.bar(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.savefig("student_marks.png")
plt.show()

print("Graph saved as student_marks.png")
