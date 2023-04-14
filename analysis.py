# This file analyses the Iris-dataset.csv file, produces some summary statistics and outputs then to a text file, 
#creates some scatter plots of the variables, and creates and saves some hisograms of each variable.
#Further info is available in the README file on GitHub.
#Author: OOS
import numpy as np
import pandas as pd 
import matplotlib.pyplot as mpl
import csv


#This block of code imports the CSV file and converts it to a pandas dataframe.
# Drawn from https://www.w3schools.com/python/pandas/pandas_csv.asp

data = pd.read_csv("Iris-dataset.csv")

summary = data.describe()
rounded_summary = np.round(summary,2)

with open("Iris Summary Information.txt", "w+") as f:
    f.write(str(rounded_summary))

# Code taken from https://www.geeksforgeeks.org/python-read-csv-columns-into-list/ and https://stackoverflow.com/questions/9012487/matplotlib-pyplot-savefig-outputs-blank-image
#This code creates lists out of the columns in the CSV datafile. 

sepal_length = data['sepal_length'].tolist()
sepal_width = data['sepal_width'].tolist()
petal_length = data['petal_length'].tolist()
petal_width = data["petal_width"].tolist()

#The following code creates and displays some (pretty) histograms 

sepal_len_hist = mpl.hist(sepal_length, color="red")
mpl.title("Sepal Length")
mpl.xlabel("Length (mm)")
mpl.ylabel("Occurences")
mpl.savefig("sepal_len_hist.png", dpi=100)
mpl.show()

sepal_width_hist = mpl.hist(sepal_width, color="blue")
mpl.title("Sepal Width")
mpl.xlabel("Width (mm)")
mpl.ylabel("Occurences")
mpl.savefig("sepal_width_hist.png", dpi=100)
mpl.show()

petal_len_hist = mpl.hist(petal_length, color="orange" )
mpl.title("Petal Length")
mpl.xlabel("Length (mm)")
mpl.ylabel("Occurences")
mpl.savefig("petal_len_hist.png", dpi=100)
mpl.show()

petal_width_hist = mpl.hist(petal_width, color="green")
mpl.title("Petal Width")
mpl.xlabel("Width (mm)")
mpl.ylabel("Occurences")
mpl.savefig("petal_width_hist.png", dpi=100)
mpl.show()

#The following code creates variables aligned to each of the four variable sin the CSV file, and plots them against one another in scatter plots.

x = np.array(sepal_width)
y = np.array(sepal_length)
z = np.array(petal_length)
a = np.array(petal_width)

scatter1 = mpl.scatter(x,y, color="red")
mpl.title("Sepal Width - Sepal Length")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
mpl.show()

scatter2 = mpl.scatter(x,z, color="blue")
mpl.title("Sepal Width - Petal Length")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
mpl.show()

scatter3 = mpl.scatter(x,a, color="orange")
mpl.title("Sepal Width - Petal Width")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
mpl.show()

scatter4 = mpl.scatter(y,z, color="green")
mpl.title("Sepal Length - Petal Length")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
mpl.show()

scatter5 = mpl.scatter(y,a, color="purple")
mpl.title("Sepal Length - Petal Width")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
mpl.show()

scatter6 = mpl.scatter(z,a, color="yellow")
mpl.title("Petal Length - Petal Width")
mpl.xlabel("Length/Width (mm)")
mpl.ylabel("Length/Width (mm)")
mpl.show()