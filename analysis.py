import numpy as np
import pandas as pd 
import matplotlib.pyplot as mpl


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

#The first block defines the historgram and defines the legend, and colors the histogram blue

x = "sepal width"
y = "sepal_length"

print(x)

scatter = mpl.scatter(x,y)
mpl.show()