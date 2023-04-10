import numpy as np
import pandas as pd 
import matplotlib.pyplot as mpl
import csv

# data = []

with open("Iris-dataset.csv") as f:
   f.read
filename = "Irises Summary.txt"

#Drawn from https://www.geeksforgeeks.org/python-read-csv-columns-into-list/

data = pd.read_csv("Iris-dataset.csv")

sepal_length = data['sepal_length'].tolist()
sepal_width = data['sepal_width'].tolist()
petal_length = data['petal_length'].tolist()
petal_length = data["petal_length"].tolist()

summary = data.describe()


with open(filename, "wt") as f:
    f.write("Iris Flowers Summary")
    f.write(str(print(summary.head())))



x = np.array(sepal_width)
y = np.array(sepal_length)

scatter = mpl.scatter(x,y)
mpl.show()