import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('sales_data.csv')

# 1) Toothpaste sales data of each month and show it using a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['month_number'], df['toothpaste'], color='blue', marker='o')
plt.title('Toothpaste Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.grid(True)
plt.show()

# 2) Face cream and face wash product sales data and show it using the bar chart
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = df['month_number']

bar1 = plt.bar(index, df['facecream'], bar_width, label='Face Cream', color='green')
bar2 = plt.bar(index + bar_width, df['facewash'], bar_width, label='Face Wash', color='orange')

plt.title('Face Cream and Face Wash Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.xticks(index + bar_width / 2, df['month_number'])
plt.legend()
plt.grid(True)
plt.show()

# Calculate total sale data for last year for each product and show it using a Pie chart
total_sales = {
    'Face Cream': df['facecream'].sum(),
    'Face Wash': df['facewash'].sum(),
    'Toothpaste': df['toothpaste'].sum(),
    'Bathing Soap': df['bathingsoap'].sum(),
    'Shampoo': df['shampoo'].sum(),
    'Moisturizer': df['moisturizer'].sum()
}

products = list(total_sales.keys())
sales_values = list(total_sales.values())

plt.figure(figsize=(8, 8))
plt.pie(sales_values, labels=products, autopct='%1.1f%%', startangle=140)
plt.title('Total Sales Data for Last Year')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()