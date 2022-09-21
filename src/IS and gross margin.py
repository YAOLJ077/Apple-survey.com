import pandas as pd
import statsmodels.api as sm
import numpy as np
import scipy.stats as stats
import statsmodels.formula.api as smf

df = pd.read_csv("../data/Linear_gross_margin_RS.csv")
df.columns = ['y', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15']
IS = df.iloc[:311, 1:16]
IS = sm.add_constant(IS)
GM = df.iloc[:311, 0]

def linear(IS, GM):
    # IS=information source and GM = gross margin
    # coefficient
    model = sm.OLS(GM,IS)
    ret1 = model.fit()
    # standardized coefficients beta
    std_err = df.select_dtypes(include=[np.number]).dropna().apply(stats.zscore)
    formula = 'y ~ x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13 + x14  + x15'
    ret2 = smf.ols(formula, data=std_err).fit()
    return ret1.summary(),ret2.summary()


if __name__ == '__main__':
    print(linear(IS, GM))



