import pandas as pd 
import matplotlib.pyplot as plt 
import sklearn 
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv('../Data/For_Profit_C2.csv')

labels = ['low', 'medium', 'standard', 'high']
# expense_bins = [0, 3000000, 6000000, 90000000, 300582000]
# salaries_bins = [0, 2500000, 4000000, 90000000, 128679000]

# df['Expense_bin'] = pd.cut(df['total_expenses'],bins=expense_bins,labels=labels)
# df['Salaries_bin'] = pd.cut(df['total_salaries'],bins=salaries_bins,labels=labels)

df['Expenses_Quantile'] = pd.qcut(df['total_expenses'], q=4, labels=labels)
df['Salaries_Quantile'] = pd.qcut(df['total_salaries'], q=4,  labels=labels)

# vectorizer = CountVectorizer()
# classifier = MultinomialNB()


counts = vectorizer.fit_transform(df['Expense_Quantile'].values.astype('U'))
targets = df['Salaries_Quantile'].values

classifier.fit(counts, targets)










