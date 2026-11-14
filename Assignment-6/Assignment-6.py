
# Assignment No. 6
# Data Preprocessing using Python

# Import Libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Step 1: Download and Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

df = pd.read_csv(url)

print("Original Dataset:")
print(df.head())
print()

# Step 2: Explore Dataset
print("Dataset Information:")
print(df.info())
print()

print("Missing Values Before Processing:")
print(df[["age", "embarked"]].isnull().sum())
print()

# Step 3: Handle Missing Values
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(
    df["embarked"].mode()[0]
)

print("Missing Values After Processing:")
print(df[["age", "embarked"]].isnull().sum())
print()

# Step 4: Encode Categorical Variables
df = pd.get_dummies(
    df,
    columns=["sex", "embarked"],
    drop_first=True,
    dtype=int
)

print("Dataset After Encoding:")
print(df.head())
print()

# Step 5: Normalize Numerical Features
scaler = MinMaxScaler()

numeric_columns = ["pclass", "age", "fare"]

df[numeric_columns] = scaler.fit_transform(
    df[numeric_columns]
)

print("Dataset After Normalization:")
print(df.head())
print()

# Step 6: Save Processed Dataset
df.to_csv("processed_titanic.csv", index=False)

print("Processed dataset saved successfully.")
print("Data preprocessing completed successfully.")
