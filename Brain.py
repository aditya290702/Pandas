import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Brain = pd.read_csv("brain_size.csv",delimiter=";")

#how many males and females are present????
gender = Brain.groupby("Gender")
print(gender.count())

#Gender-Wise VIQ count
print(gender["VIQ"].count())

#Gender-wise MRI MEAN
print(np.log2(gender["MRI_Count"].mean()))

#pd.plotting.scatter_matrix(Brain[["Weight","Height","MRI_Count"]])
#plt.show()


#pd.plotting.scatter_matrix(Brain[["PIQ","VIQ","FSIQ"]])
#plt.show()

#--------------------------------------------------------------------------------------

print(stats.ttest_1samp(Brain["VIQ"],0))
female_viq = Brain[Brain["Gender"] == "Male"] ["VIQ"]
male_viq = Brain[Brain["Gender"] == "Male"] ["VIQ"]

print(stats.ttest_ind(female_viq,male_viq))