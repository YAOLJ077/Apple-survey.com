import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("../data/Binary_Technology_RS.csv")
df['intercept'] = 1.0
# print(df.columns)
# print(df.head())
dum1 = pd.get_dummies(df[])