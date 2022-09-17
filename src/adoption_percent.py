import pandas as pd
def adoption_percent():

    df_RS = pd.read_csv("F:/Python/Apple-survey.com/data/RS_adoption.csv")
    a = df_RS.sum()
    b = df_RS.count()
    p = a / b * 100
    return p

if __name__=='__main__':
    adoption_percent()
    print(adoption_percent())

