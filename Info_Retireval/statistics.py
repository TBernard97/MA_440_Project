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

labels = ['low', 'medium', 'high', 'very high']
bins = [-30859103.721,  6195393823.2, 12390670367.4,18585946911.6, 24781223455.8 ]

data['expenses_bins'] = pd.cut(expenses, bins, labels=labels)


#tuition_bins = pd.cut(tuition , 5, labels=labels)

print(data)