import pandas as pd 


df = pd.read_csv('../Data/For-Profit-C1.csv')

labels = ['low', 'medium', 'standard', 'high']
expense_bins = [0, 3000000, 6000000, 90000000, 300582000]
salaries_bins = [0, 2500000, 4000000, 90000000, 128679000]

df['Expense_bin'] = pd.cut(df['total_expenses'],bins=expense_bins,labels=labels)
df['Salaries_bin'] = pd.cut(df['total_salaries'],bins=salaries_bins,labels=labels)




print(df)

