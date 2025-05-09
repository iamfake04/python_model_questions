import pandas as pd

# Load the CSV file
df = pd.read_csv('auto.csv')

# 1) Clean and Update the CSV file
# Assuming the CSV might have missing values or inconsistent data types, we will clean it

# Drop rows with any missing values
df.dropna(inplace=True)

# Convert data types if necessary
df['index'] = df['index'].astype(int)
df['wheel-base'] = df['wheel-base'].astype(float)
df['length'] = df['length'].astype(float)
df['horsepower'] = df['horsepower'].astype(float)
df['average-mileage'] = df['average-mileage'].astype(float)
df['price'] = df['price'].astype(float)

# Save the cleaned data back to the CSV file
df.to_csv('auto_cleaned.csv', index=False)

# 2) Print total cars of all companies
total_cars_by_company = df['company'].value_counts()
print("Total cars of all companies:")
print(total_cars_by_company)

# 3) Find the average mileage of all companies
average_mileage_by_company = df.groupby('company')['average-mileage'].mean()
print("\nAverage mileage of all companies:")
print(average_mileage_by_company)

# 4) Find the highest priced car of all companies
highest_priced_car_by_company = df.groupby('company').apply(lambda x: x.loc[x['price'].idxmax()])
print("\nHighest priced car of all companies:")
print(highest_priced_car_by_company[['company', 'price']])