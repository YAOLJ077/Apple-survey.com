from itertools import count
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("/Users/zhouliyun/Desktop/apple/Apple-survey.com/data/data_final.xlsx")
Age = df["Age"].value_counts()
Area = df["Area"].value_counts()
Edu = df["Edu"].value_counts()

Gender = df["Sex"].value_counts()
Training = df["Training"].value_counts()
FC = df["Farm Cooperative"].value_counts()
PK = df["Pesticide Knowledge"].value_counts()
PA = df["Prevention Awareness"].value_counts()

print(len(list(pd.DataFrame(Age).iloc[:,0])))
print(len(list(pd.DataFrame(Age).index)))

plt.plot(list(pd.DataFrame(Age).index),list(pd.DataFrame(Age).iloc[:,0]))
plt.show()
# for age in Age:
#     count = Age[age]
#     print(list(count))


# ax1 = plt.subplot(3,1,1)
# plt.bar(md["Age"], height=md["Age"], color="r")
# ax2 = plt.subplot(3,2,2)
# plt.bar(md["Edu"], height=md["Edu"], color="y")
# ax3 = plt.subplot(3,2,3)
# plt.bar(md["Area"], height=md["Area"], color="g")
# plt.show()