import pandas as pd
url="https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv"
data=pd.read_csv(url)
data
#y=w*x+b
x=data["YearsExperience"]
y=data["Salary"]

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show