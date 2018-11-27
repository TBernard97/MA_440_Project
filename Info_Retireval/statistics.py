import pandas as pd 

data = pd.read_csv("../Data/tui_exp_sal.csv")

tuition = data['tuition_and_fees']
expenses = data['total_expenses']
salaries = data['total_salaries']

tuition_AVG = tuition.mean()
tuition_MAX = tuition.max()
tuition_MIN = tuition.min()

expenses_AVG = expenses.mean()
expenses_MAX = expenses.max()
expenses_MIN = expenses.min()

print("[STAT] TUITION MEAN : {} TUITION MAX : {} TUITION MIN : {}".format(tuition_AVG, tuition_MAX, tuition_MIN))
print("[STAT] EXPENSES MEAN : {} EXPENSES MAX : {} EXPENSES MIN : {}".format(expenses_AVG, expenses_MAX, expenses_MIN))

expenses_bins = pd.cut(expenses, 5)
expenses_groups = expenses.groupby(expenses_bins).agg(['count', 'sum'])
print(expenses_groups)

tuition_bins = pd.cut(tuition , 5)
tuition_groups = tuition.groupby(tuition_bins).agg(['count', 'sum'])
print(tuition_groups)