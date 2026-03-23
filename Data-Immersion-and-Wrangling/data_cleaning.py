import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

print("Initial Dataset:")
print(df.head())

# 1. Remove duplicates
df.drop_duplicates(inplace=True)

# 2. Handle missing values
df['Price'].fillna(df['Price'].mean(), inplace=True)
df['City'].fillna("Unknown", inplace=True)

# 3. Standardize date format
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce', dayfirst=True)
df['Date_of_Birth'] = pd.to_datetime(df['Date_of_Birth'], errors='coerce', dayfirst=True)

# 4. Feature Engineering
df['Total_Sales'] = df['Quantity'] * df['Price']
df['Customer_Age'] = 2026 - df['Date_of_Birth'].dt.year

# 5. Remove outliers (Quantity > 1000)
df = df[df['Quantity'] < 1000]

# Save cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("\nCleaned Dataset:")
print(df.head())