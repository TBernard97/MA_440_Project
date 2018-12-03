import pandas as pd 
import matplotlib.pyplot as plt 



df = pd.read_csv('../Data/For_Profit_C2.csv')

labels = ['low', 'medium', 'standard', 'high']

tuition_bin = [0, 3000000, 6000000, 8000000, 300582000]
expense_bins = [0, 3000000, 6000000, 90000000, 300582000]
salaries_bins = [0, 2500000, 4000000, 90000000, 128679000]
grants_bins = [0, 800000, 4000000, 7000000, 53263100]


df['Tuition_bin'] = pd.cut(df['tuition_and_fees'], bins=tuition_bin, labels=labels)
df['Expense_bin'] = pd.cut(df['total_expenses'],bins=expense_bins,labels=labels)
df['Salaries_bin'] = pd.cut(df['total_salaries'],bins=salaries_bins,labels=labels)
df['Grants_bin'] = pd.cut(df['pell_grants'], bins=grants_bins, labels=labels)


df.to_csv('../Data/For-Profit-C2_Binned.csv')

print(df)