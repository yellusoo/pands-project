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

sepal_len_hist = mpl.hist(sepal_length, color="red")
mpl.title("Sepal Length")
mpl.xlabel("Length (mm)")
mpl.ylabel("Occurences")
mpl.savefig("sepal_len_hist.png", dpi=100)
#mpl.show()

sepal_width_hist = mpl.hist(sepal_width, color="blue")
mpl.title("Sepal Width")
mpl.xlabel("Width (mm)")
mpl.ylabel("Occurences")
mpl.savefig("sepal_width_hist.png", dpi=100)
#mpl.show()

petal_len_hist = mpl.hist(petal_length, color="orange" )
mpl.title("Petal Length")
mpl.xlabel("Length (mm)")
mpl.ylabel("Occurences")
mpl.savefig("petal_len_hist.png", dpi=100)
#mpl.show()

petal_width_hist = mpl.hist(petal_width, color="green")
mpl.title("Petal Width")
mpl.xlabel("Width (mm)")
mpl.ylabel("Occurences")
mpl.savefig("petal_width_hist.png", dpi=100)
#mpl.show()

x = np.array(sepal_width)
y = np.array(sepal_length)
z = np.array(petal_length)
a = np.array(petal_width)

scatter1 = mpl.scatter(x,y, color="red")
mpl.title("Sepal Width - Sepal Length")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
#mpl.show()

scatter2 = mpl.scatter(x,z, color="blue")
mpl.title("Sepal Width - Petal Length")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
#mpl.show()

scatter3 = mpl.scatter(x,a, color="orange")
mpl.title("Sepal Width - Petal Width")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
#mpl.show()

scatter4 = mpl.scatter(y,z, color="green")
mpl.title("Sepal Length - Petal Length")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
#mpl.show()

scatter5 = mpl.scatter(y,a, color="purple")
mpl.title("Sepal Length - Petal Width")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
#mpl.show()

scatter6 = mpl.scatter(z,a, color="yellow")
mpl.title("Petal Length - Petal Width")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
#mpl.show()


sepal_length_mean = np.mean(sepal_length)
sepal_width_mean = np.mean(sepal_width)
petal_length_mean = np.mean(petal_length)
petal_width_mean = np.mean (petal_width)

means = sepal_length_mean, sepal_width_mean, petal_length_mean, petal_width_mean
print(means)

with open("Iris Summary Information.txt", "w+") as f:
    f.write(str("Average Sepal Length, Sepal Width, Petal Length and Petal Width are (in mm)"))
    f.write(str(means))