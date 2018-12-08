import pandas as pd 
import matplotlib.pyplot as plt 

#INPUT FILE
df = pd.read_csv('../Data/For-Profit-Financial-POOL.csv')

#LABEL MODIFICATION
tuition_labels = ['tuition_low', 'tuition_medium', 'tuition_standard', 'tuition_high']
expense_labels = ['expense_low', 'expense_medium', 'expense_standard', 'expense_high']
salaries_labels = ['salaries_low', 'salaries_medium', 'salaries_standard', 'salaries_high']
grants_labels  = ['grants_low', 'grants_medium', 'grants_standard', 'grants_high']
retention_labels = ['retention_low', 'retention_medium', 'retention_standard', 'retention_high']


#NEW COLUMNS

#CHANGE THE LABELS => kwarg to wahtever label mod made

#The qcut df is whatever column is in your table
df['Tuition_Quantile']  = pd.qcut(df['tuition_and_fees'], q=4, labels=tuition_labels)
df['Expense_Quantile']  = pd.qcut(df['total_expenses'], q=4, labels=expense_labels)
df['Salaries_Quantile'] = pd.qcut(df['total_salaries'], q=4, labels=salaries_labels)
df['Grants_Quantile']   = pd.qcut(df['pell_grants'], q=4, labels=grants_labels)
df['Retention_Quantile']= pd.qcut(df['retention_rate_ft'], q=4, labels=retention_labels)

#OUTPUT FILE
df.to_csv('../Data/For-Profit-NOM.csv')

print(df) 