import numpy as np
import pandas as pd 

#Drawn from https://stackoverflow.com/questions/33889310/r-summary-equivalent-in-numpy

data = pd.read_csv("Iris-dataset.csv", sep= ",")
data.head()

summary = data.describe()



with open("Iris-dataset.csv") as f:
    f.read
filename = "Irises Summary.txt"
with open(filename, "wt") as f:
    f.write("Iris Flowers Summary")
    f.write(str(print(summary.head())))
