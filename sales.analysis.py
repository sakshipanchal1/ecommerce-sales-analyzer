import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Step 1: Simulate Sample E-Commerce Dataset
np.random.seed(42)
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books']
regions = ['North', 'South', 'East', 'West']

data = {
    'Order_ID': range(1001, 1201),
    'Category': np.random.choice(categories, 200),
    'Region': np.random.choice(regions, 200),
    'Quantity': np.random.randint(1, 5, 200),
    'Unit_Price': np.random.uniform(200, 5000, 200).round(2),
    'Discount': np.random.choice([0.0, 0.05, 0.1, 0.2], 200, p=[0.5, 0.3, 0.1, 0.1]),
}

df = pd.DataFrame(data)

# Step 2: Data Cleaning & Feature Engineering
df['Total_Sales'] = (df['Quantity'] * df['Unit_Price']) * (1 - df['Discount'])
df['Total_Sales'] = df['Total_Sales'].round(2)

# Assume profit is 30% of sales minus discount impact
df['Profit'] = (df['Total_Sales'] * np.random.uniform(0.1, 0.4, 200)).round(2)

print('--- First 5 Rows of Processed Data ---')
print(df.head())

# Step 3: Business Insights / Aggregations
print('\n--- Total Sales & Profit by Category ---')
category_summary = (
    df.groupby('Category')[['Total_Sales', 'Profit']].sum().round(2)
)
print(category_summary)

print('\n--- Regional Performance ---')
region_summary = df.groupby('Region')[['Total_Sales', 'Profit']].sum().round(2)
print(region_summary)

# Step 4: Data Visualization
plt.figure(figsize=(10, 5))

# Sales by Category Chart
plt.subplot(1, 2, 1)
category_summary['Total_Sales'].plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.ylabel('Sales (INR)')
plt.xticks(rotation=45)

# Profit by Category Chart
plt.subplot(1, 2, 2)
category_summary['Profit'].plot(kind='bar', color='lightgreen')
plt.title('Total Profit by Category')
plt.ylabel('Profit (INR)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('sales_analysis_chart.png')
print(
    '\n[Success] Analysis complete! Chart saved as "sales_analysis_chart".'
)
