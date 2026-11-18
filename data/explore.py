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