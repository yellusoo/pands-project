import numpy as np
import pandas as pd 
import matplotlib.pyplot as mpl
import csv

#Drawn from https://www.geeksforgeeks.org/python-read-csv-columns-into-list/

data = pd.read_csv("Iris-dataset.csv")


sepal_length = data['sepal_length'].tolist()
sepal_width = data['sepal_width'].tolist()
petal_length = data['petal_length'].tolist()
petal_width = data["petal_width"].tolist()


x = np.array(sepal_width)
y = np.array(sepal_length)

scatter = mpl.scatter(x,y)
# mpl.show()

with open("Iris Summary Information.txt", "w") as f:
    f.write(str(print(sepal_length)))