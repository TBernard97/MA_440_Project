import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
from apyori import apriori

uni_data = pd.read_csv('../Data/For-Profit-C2_NOM.csv')

records = []

for i in range(0,42):
    records.append([str(uni_data.values[i,j]) for j in range(0,3)])

association_rules = apriori(records, min_support = 0.067, min_confidence=0.2, min_lift=1)

association_results = list(association_rules)

print(association_results[0])

for uni in association_results:

    pair = uni[0]
    unis = [x for x in pair]

    print("Rule: " + str(unis))
    print("Support : " + str(uni[1]))

    print("Confidence " + str(uni[2][0][2]))
    print("Lift: " + str(uni[2][0][3]))
    print("====================================")