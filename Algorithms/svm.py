import pandas as pd 
import numpy as np 
from sklearn import svm 
import matplotlib.pyplot as plt
import seaborn as sns


table = pd.read_csv(r"/Users/AES_NOMAD/Documents/MA440/MA440_Project/Data/tuition_expenses.csv")

cost = table['tuition_and_fees']
expenses = table['total_expenses']




