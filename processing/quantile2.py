import pandas as pd 
import matplotlib.pyplot as plt 


#Input
df = pd.read_csv('Set2filter.csv')

tuition_labels = ['tuition_low', 'tuition_medium', 'tuition_standard', 'tuition_high']
investment_labels = ['investment_low', 'investment_medium', 'investment_standard', 'investment_high']
expenses_labels = ['expenses_low', 'expenses_medium', 'expenses_standard', 'expenses_high']



df['Tuition_Quantile']  = pd.qcut(df['tuition_and_fees'], q=4, labels=tuition_labels, duplicates='drop')
df['Investment_Quantile']  = pd.qcut(df['investment_income'], q=4, labels=investment_labels, duplicates='drop')
df['Expenses_Quantile'] = pd.qcut(df['total_expenses'], q=4, labels=expenses_labels,duplicates='drop')

#Output
df.to_csv('Set2filter_binned.csv')

print(df) 