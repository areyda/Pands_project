# PANDS Project 2021 - Investigation and Analysis of the Iris Dataset. 
# The output for this code is included in the summary.txt file
# Summary of Investigation and Analysis is included in the READ.md file
# Author - Amy Reynolds 

# Import libaries below: 
from numpy.core.arrayprint import str_format
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as py
import io

# Import the dataset - The dataframe (df) is where pd (pandas library) reads the iris csv file. 
# The dataframe could also have been imported by including the relevant URL in the string format.
df = pd.read_csv("iris.csv")

#  Setting Dataframes per Iris Variety and inclusion of the unit of measurement with the columns: 
Setdf = df.loc[df["variety"] == "Setosa"]
Setdf.columns = ["Sepal Length(cm)", "Sepal Width(cm)", "Petal Length(cm)", "Petal Width(cm)", "Variety"]
Verdf = df.loc[df["variety"] == "Versicolor"]
Verdf.columns = ["Sepal Length(cm)", "Sepal Width(cm)", "Petal Length(cm)", "Petal Width(cm)", "Variety"]
Virdf = df.loc[df["variety"] == "Virginica"]
Virdf.columns = ["Sepal Length(cm)", "Sepal Width(cm)", "Petal Length(cm)", "Petal Width(cm)", "Variety"]

# Dataframe columns as per string inclusion of the unit of measurement with the columns: 
df.columns = ["Sepal Length(cm)", "Sepal Width(cm)", "Petal Length(cm)", "Petal Width(cm)", "Variety"]
# Dataframe grouped by Variety 
grouped = df.groupby("Variety")

# Setting output file to filename
filename = "summary.txt"



# DATASET INVESTIGATION AND ANALYSIS - See output file - summary.txt

# Display the shape of the dataframe - number of rows and columns for the dataset
Shape = df.shape
with open (filename, "w") as f:
    f.write ("Dataframe Shape: "  )
    f.write (str(Shape))
    f.write ('\n\n\n')

# Display the # of rows associated for each of the variables. 
Count = df.groupby("Variety").size()
with open (filename, "a") as f:
    f.write ("Number of rows associated with each variable: \n")
    f.write (str(Count))
    f.write ('\n\n\n')

# Display the data types and basic information associated with the dataset 
Types = df.dtypes
with open (filename, "a") as f:
    f.write ("Dataset data types: \n")
    f.write (str(Types))
    f.write ("\n\n\n")

# Display information about dataset
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
with open (filename, "a") as f: 
    f.write ("Iris Dataset Information: \n")
    f.write ((s))
    f.write ("\n\n")

## https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html

# Verify that null values are absent 
Null = df.isnull().sum()
with open (filename, "a") as f:
    f.write ("Null Value Check: \n\n")
    f.write (str(Null))
    f.write ("\n\n")

# Duplicate Verification 
SumDup = df.duplicated().sum()
with open (filename, "a") as f: 
    f.write ("Duplicate Verification\n" "Number of Duplicate Values: ")
    f.write (str(SumDup))
    f.write ("\n\n")

Dup = df[df.duplicated()]
with open (filename,"a") as f:
    f.write ("Row")
    f.write (str(Dup))
    f.write ("\n\n")


# Display the first 5 rows of the dataset
Head = df.head()
with open (filename, "a") as f:
    f.write ("First 5 Rows of Dataset: \n\n")
    f.write (str(Head))
    f.write ("\n\n")


# Display the last 5 rows of the dataset
Tail = df.tail()
with open (filename, "a") as f: 
    f.write ("Last 5 Rows of Dataset: \n\n")
    f.write (str(Tail))
    f.write ("\n\n\n")


# Display random sample (15) of the dataset
Sample = df.sample(15)
with open (filename, "a") as f:
    f.write ("Random Sample of 15 Rows: \n\n")
    f.write (str(Sample))
    f.write ("\n\n\n")


# Display the dataset statistic characteristics - total dataset 
Desc = df.describe(include = "all")
with open (filename, "a") as f: 
    f.write ("Statistical Characteristics - Total Dataset: \n\n")
    f.write (str(Desc))
    f.write ("\n\n\n")


# Display the dataset statistic characteristics - Setosa
SDesc = Setdf.describe()
with open (filename, "a") as f: 
    f.write ("Statistical Characteristics - Setosa Variety: \n\n")
    f.write (str(SDesc))
    f.write ("\n\n\n")


# Display the dataset statistic characteristics - Versicolor 
VerDesc = Verdf.describe()
with open (filename, "a") as f: 
    f.write ("Statistical Characteristics - Versicolor Variety: \n\n")
    f.write (str(VerDesc))
    f.write ("\n\n\n")


# Display the dataset statistic characteristics - Virginica 
VirDesc = Virdf.describe()
with open (filename, "a") as f: 
    f.write ("Statistical Characteristics - Virginica Variety: \n\n")
    f.write (str(VirDesc))
    f.write ("\n\n\n")


# Display the Data Correlation - Total Dataset 
TCorr = df.corr()
with open (filename, "a") as f:
    f.write ("Data Correlation - Total Dataset: \n\n")
    f.write (str(TCorr))
    f.write ("\n\n\n")


# Display the Data Correlation - Setosa Variety  
SCorr = Setdf.corr()
with open (filename, "a") as f:
    f.write ("Data Correlation - Setosa Variety: \n\n")
    f.write (str(SCorr))
    f.write ("\n\n\n")


# Display the Data Correlation - Versicolor Variety  
VerCorr = Verdf.corr()
with open (filename, "a") as f:
    f.write ("Data Correlation - Versicolor Variety: \n\n")
    f.write (str(VerCorr))
    f.write ("\n\n\n")


# Display the Data Correlation - Virginica Variety  
VirCorr = Virdf.corr()
with open (filename, "a") as f:
    f.write ("Data Correlation - Virginica Variety: \n\n")
    f.write (str(VirCorr))
    f.write ("\n\n\n")


# DATA VISUALIZATION 

# Histogram - Generate and save - All Varieties
df.hist(figsize = (8,6))
plt.suptitle ("Iris Dataset Histogram")
plt.savefig("PNG\Hist_All.png")

# Histogram - Generate and save - Setosa Variety 
Setdf.hist(figsize = (8,6))
plt.suptitle ("Iris Data Histogram - Setosa Variety")
plt.savefig("PNG\Hist_Setosa.png")

# Histogram - Generate and save - Versicolor Variety 
Verdf.hist(figsize = (8,6))
plt.suptitle ("Iris Data Histogram - Versicolor Variety")
plt.savefig("PNG\Hist_Versicolor.png")

# Histogram - Generate and save - Virginica Variety 
Virdf.hist(figsize = (8,6))
plt.suptitle ("Iris Data Histogram - Virginica Variety")
plt.savefig("PNG\Hist_Virginica.png")


