import pandas as pd 
import matplotlib.pyplot as plt 



df = pd.read_csv('../Data/For_Profit_C2.csv')

labels = ['low', 'medium', 'standard', 'high']


df['Tuition_Quantile']  = pd.qcut(df['tuition_and_fees'], q=4, labels=labels)
df['Expense_Quantile']  = pd.qcut(df['total_expenses'], q=4, labels=labels)
df['Salaries_Quantile'] = pd.qcut(df['total_salaries'], q=4, labels=labels)
df['Grants_Quantile']   = pd.qcut(df['pell_grants'], q=4, labels=labels)
df['Retention_Quantile']= pd.qcut(df['retention_rate_ft'], q=4, labels=labels)

df.to_csv('../Data/For-Profit-C2_Tiled.csv')

print(df)