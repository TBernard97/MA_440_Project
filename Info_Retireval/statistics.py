import pandas as pd 

data = pd.read_csv("../Data/tui_exp_sal.csv")

tuition = data['tuition_and_fees']
expenses = data['total_expenses']
salaries = data['total_salaries']

print(tuition)