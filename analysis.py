# PANDS Project 2021 - Investigation and Analysis of the Iris Dataset. 
# Author - Amy Reynolds 

# Import libaries below: 
from numpy.core.arrayprint import str_format
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as py

# Import the dataset - The dataframe (df) is where pd (pandas library) reads the iris csv file. 
# The dataframe could also have been imported by including the relevant URL in the string format.
df = pd.read_csv("iris.csv")

# Dataframe columns as per string
df.columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Variety"]
# Dataframe grouped by Variety 
grouped = df.groupby("Variety")

filename = "summary.txt"

# Display the shape of the dataframe - number of rows and columns for the dataset
Shape = df.shape
with open (filename, "w") as f:
    f.write ("Dataframe Shape: "  )
    f.write (str(Shape))
    f.write ('\n\n\n')

# Display the # of rows associated for each of the variables. 
Count = df.groupby("Variety").size()
with open (filename, "a") as f:
    f.write ("Number of rows for each variable: \n")
    f.write (str(Count))
    f.write ('\n\n\n')

# Display the data types and basic information associated with the dataset 
Types = df.dtypes
with open (filename, "a") as f:
    f.write ("Dataset data types: \n")
    f.write (str(Types))
    f.write ("\n\n\n")

# Display a portion and provide information about dataset
Info = df.info()
with open (filename, "a") as f: 
    f.write ("Sample of Iris Dataset: \n")
    f.write (str(Info))
    f.write ("\n\n\n")





