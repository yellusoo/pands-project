import numpy as np
import pandas as pd 
import matplotlib.pyplot as mpl
import csv



# Drawn from https://www.w3schools.com/python/pandas/pandas_csv.asp



data = pd.read_csv("Iris-dataset.csv")

# Code taken from https://www.geeksforgeeks.org/python-read-csv-columns-into-list/ and https://stackoverflow.com/questions/9012487/matplotlib-pyplot-savefig-outputs-blank-image

sepal_length = data['sepal_length'].tolist()
sepal_width = data['sepal_width'].tolist()
petal_length = data['petal_length'].tolist()
petal_width = data["petal_width"].tolist()

sepal_len_hist = mpl.hist(sepal_length)
mpl.xlabel("Length")
mpl.ylabel("Occurences")

mpl.savefig("sepal_len_hist.png", dpi=100)
sepal_width_hist = mpl.hist(sepal_width)
mpl.savefig("sepal_width_hist.png", dpi=100)
petal_len_hist = mpl.hist(petal_length)
mpl.savefig("petal_len_hist.png", dpi=100)
petal_width_hist = mpl.hist(petal_width)
mpl.savefig("petal_width_hist.png", dpi=100)

x = np.array(sepal_width)
y = np.array(sepal_length)
z = np.array(petal_length)
a = np.array(petal_width)

scatter1 = mpl.scatter(x,y)
mpl.show()
scatter2 = mpl.scatter(x,z)
mpl.show()
scatter3 = mpl.scatter(x,a)
mpl.show()
scatter4 = mpl.scatter(y,z)
mpl.show()
scatter5 = mpl.scatter(y,a)
mpl.show()
scatter6 = mpl.scatter(z,a)
mpl.show()

with open("Iris Summary Information.txt", "w+") as f:
    f.write(str(print(sepal_length)))
    f.write(str(print(data.describe)))   
    
