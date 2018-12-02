import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
from apyori import apriori

uni_data = pd.read_csv('../Data/tui_exp_sal.csv')

records = []

for i in range(0,10):
    records.append([str(uni_data.values[i,j]) for j in range(0,4)])

association_rules = apriori(records, min_support = 0.0045, min_confidence=0.2, min_lift=3, min_length=2)

association_results = list(association_rules)

print(association_results[0])