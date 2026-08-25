import pandas as pd

df = pd.read_csv("data/hr_employee_attrition.csv")

print("Dataset loaded successfully!")
print("\nRows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())