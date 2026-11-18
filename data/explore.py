""" Lab 13 - Angelo Caruso

Self-assessment

1. Without looking at your code, can you explain what a boolean filter does in plain English? Practice saying it out loud.

2. What is the difference between df["revenue"] and df[["revenue"]]? When does the distinction matter?

3. If a colleague who only knows Excel asked you to explain why you would choose pandas for this task, what is the single most compelling reason you would give? 

"""

# ----- Exercise 1 -----

import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

#Inspection Commands
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# ----- Exercise 2 -----

south = df[df['region'] == 'South']

print(len(south))
print(south.head())

# ----- Exercise 3 -----

top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

# ----- Exercise 4 -----

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())

# ---- Exercise 5 -----

df['per_unit'] = df['revenue'] / df['quantity']
print(df[['per_unit']].head())
print(df['per_unit'].mean())

# ----- Exercise 6 -----

# Method 1
print(df['region'].unique())

# Method 2
print(df['region'].value_counts())

# ----- Exercise 7 -----

df_subset = df[['region', 'product', 'revenue']]

print(df_subset.shape)

# ----- Exercise 8 -----

df.to_csv('data/explored.csv', index=False)