# PANDS Project 2021 - Investigation and Analysis of the Iris Dataset. 
# summary.txt file provides the output for this code below. 
# READ.md file provides the results for the Investigation and Analysis 
# Author - Amy Reynolds 

# Import libaries below: 
from numpy.core.arrayprint import str_format
from numpy.matrixlib import defmatrix
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as py
import io

# Import the dataset - The dataframe (df) is where pd (pandas library) reads the iris csv file. 
# The dataframe could also have been imported by including the relevant URL in the string format.
df = pd.read_csv("iris.csv")

#  Setting Dataframes per Iris Variety and inclusion of the unit of measurement with the columns: 
Set = df.loc[df["variety"] == "Setosa"]
Set.columns = ["Sepal Length(cm)", "Sepal Width(cm)", "Petal Length(cm)", "Petal Width(cm)", "Variety"]
Ver = df.loc[df["variety"] == "Versicolor"]
Ver.columns = ["Sepal Length(cm)", "Sepal Width(cm)", "Petal Length(cm)", "Petal Width(cm)", "Variety"]
Vir = df.loc[df["variety"] == "Virginica"]
Vir.columns = ["Sepal Length(cm)", "Sepal Width(cm)", "Petal Length(cm)", "Petal Width(cm)", "Variety"]

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
SDesc = Set.describe()
with open (filename, "a") as f: 
    f.write ("Statistical Characteristics - Setosa Variety: \n\n")
    f.write (str(SDesc))
    f.write ("\n\n\n")


# Display the dataset statistic characteristics - Versicolor 
VerDesc = Ver.describe()
with open (filename, "a") as f: 
    f.write ("Statistical Characteristics - Versicolor Variety: \n\n")
    f.write (str(VerDesc))
    f.write ("\n\n\n")


# Display the dataset statistic characteristics - Virginica 
VirDesc = Vir.describe()
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
SCorr = Set.corr()
with open (filename, "a") as f:
    f.write ("Data Correlation - Setosa Variety: \n\n")
    f.write (str(SCorr))
    f.write ("\n\n\n")


# Display the Data Correlation - Versicolor Variety  
VerCorr = Ver.corr()
with open (filename, "a") as f:
    f.write ("Data Correlation - Versicolor Variety: \n\n")
    f.write (str(VerCorr))
    f.write ("\n\n\n")


# Display the Data Correlation - Virginica Variety  
VirCorr = Vir.corr()
with open (filename, "a") as f:
    f.write ("Data Correlation - Virginica Variety: \n\n")
    f.write (str(VirCorr))
    f.write ("\n\n\n")


# DATA VISUALIZATION - Matplotlib

# Histogram - Generate and save - All Varieties
df.hist(figsize = (8,6))
plt.suptitle ("Iris Dataset Histogram")
plt.savefig("PNG\Hist_All.png")

# Histogram - Generate and save - Setosa Variety 
Set.hist(figsize = (8,6))
plt.suptitle ("Iris Data Histogram - Setosa Variety")
plt.savefig("PNG\Hist_Setosa.png")

# Histogram - Generate and save - Versicolor Variety 
Ver.hist(figsize = (8,6))
plt.suptitle ("Iris Data Histogram - Versicolor Variety")
plt.savefig("PNG\Hist_Versicolor.png")

# Histogram - Generate and save - Virginica Variety 
Vir.hist(figsize = (8,6))
plt.suptitle ("Iris Data Histogram - Virginica Variety")
plt.savefig("PNG\Hist_Virginica.png")

##https://www.geeksforgeeks.org/how-to-set-a-single-main-title-for-all-the-subplots-in-matplotlib/

# Need to review the scatterplots from matplotlib...


# Scatterplot - Generate and save - All Varieties
plt.scatter(df["Petal Length(cm)"], df["Petal Width(cm)"])
plt.title ("Petal Length vs. Petal Width - All Species")
plt.xlabel ("Petal Length (cm)")
plt.ylabel ("Petal Width (cm)")
plt.show()


plt.scatter(df["Sepal Length(cm)"], df["Sepal Width(cm)"])
plt.title ("Sepal Length vs. Sepal Width - All Species")
plt.xlabel ("Sepal Length (cm)")
plt.ylabel ("Sepal Width (cm)")
plt.show()

# Scatterplot - Generate and save - Setosa Variety 
plt.scatter(Set["Petal Length(cm)"], Set["Petal Width(cm)"])
plt.title ("Petal Length vs. Petal Width - Setosa")
plt.xlabel ("Petal Length (cm)")
plt.ylabel ("Petal Width (cm)")
plt.show()

plt.scatter(Set["Sepal Length(cm)"], Set["Sepal Width(cm)"])
plt.title ("Sepal Length vs. Sepal Width - Setosa")
plt.xlabel ("Sepal Length (cm)")
plt.ylabel ("Sepal Width (cm)")
plt.show()


# Scatterplot - Generate and save - Versicolor Variety 
plt.scatter(Ver["Petal Length(cm)"], Ver["Petal Width(cm)"])
plt.title ("Petal Length vs. Petal Width - Versicolor")
plt.xlabel ("Petal Length (cm)")
plt.ylabel ("Petal Width (cm)")
plt.show()

plt.scatter(Ver["Sepal Length(cm)"], Ver["Sepal Width(cm)"])
plt.title ("Sepal Length vs. Sepal Width - Versicolor")
plt.xlabel ("Sepal Length (cm)")
plt.ylabel ("Sepal Width (cm)")
plt.show()


# Scatterplot - Generate and save - Virginica Variety 
plt.scatter(Vir["Petal Length(cm)"], Vir["Petal Width(cm)"])
plt.title ("Petal Length vs. Petal Width - Virginica")
plt.xlabel ("Petal Length (cm)")
plt.ylabel ("Petal Width (cm)")
plt.show()

plt.scatter(Vir["Sepal Length(cm)"], Vir["Sepal Width(cm)"])
plt.title ("Sepal Length vs. Sepal Width - Virginica")
plt.xlabel ("Sepal Length (cm)")
plt.ylabel ("Sepal Width (cm)")
plt.show()

# DATA VISUALIZATION - Seaborn
# Scatterplot - Generate and save - All Varieties - Petal Length vs Petal Width
sns.scatterplot (x ="Petal Length(cm)", y="Petal Width(cm)", hue= "Variety",data = df)
plt.title ("Scatterplot Petal Length vs. Petal Width - All Varieties")
plt.show()

# Scatterplot - Generate and save - All Varieties - Sepal Length vs Sepal Width
sns.scatterplot (x="Sepal Length(cm)", y="Sepal Width(cm)", hue="Variety",data = df)
plt.title ("Scatterplot Sepal Length vs. Sepal Width - All Varieties")
plt.show()

# Pairplot - All Varieties 
sns.pairplot(df, hue="Variety")
plt.subplots_adjust(top=0.95)
plt.suptitle ("Pairplot of the Iris Dataset")
plt.show()

##https://stackoverflow.com/questions/28638158/seaborn-facetgrid-how-to-leave-proper-space-on-top-for-suptitle


##Histogram for each variable - Generate and save - All Varieties 
sns.histplot(x="Petal Length(cm)", hue="Variety", data = df)
plt.show()

sns.histplot(x="Petal Width(cm)",  hue="Variety", data = df)
plt.show()

sns.histplot(x="Sepal Length(cm)", hue="Variety", data = df)
plt.show()

sns.histplot(x="Sepal Width(cm)",  hue="Variety", data = df)
plt.show()


