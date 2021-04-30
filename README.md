# Programming and Scripting 2021 - Project - Iris Dataset
The purpose of this repository is to document the research and investigation of the well-known Iris Dataset. 

## Project Outline and Objectives
The project consisted of the following: 
* Research the Iris Dataset online and write a summary. 
* Download the Iris Dataset and add it to the repository. 
* Write a program called analysis.py that:  
  * Outputs a summary of each variable to a single text file. 
  * Save a histogram of each variable to .png files.
  * Output a scatter plot of each pair of variables. 



# 1. Introduction 

The Iris dataset, also known as the Fisher's Iris dataset was generated by Sir Ronald Fisher, a British statistician and biologist. The multivariate dataset was published in the 1936 paper titled "The use of Multiple Measurements in Taxonomic Problems". The purpose in the analysis of the data was to allow Fisher to develop and evaluate a linear discriminant model in order to distinguish between different species of the Iris flower based the measurement of certain attributes or features. 
In the paper, Fischer credited Dr. Edgar Anderson on gathering the data. Two of the three species were collected in the Gaspe Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus.[[1]](https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-anderson36-2)[[2]](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)

The complete dataset consists of 150 rows, representing 50 samples taken for each of the selected Iris flower species (setosa, versicolor and virginica). For each sample, the sepal length, sepal width, petal length and petal width measurements in centimeters were obtained. These measurements are displayed in the dataset as a floating value. One species of the Iris flower (setosa) is considered to be linearly separable from the other two (versicolor and virginica), but the other two are not linearly separable from one another. 

This dataset is widely available online to download for analysis. It is considered a relatively simple dataset yet a very useful dataset for illustrating various ideas in data science and within machine learning. The dataset is often used in data mining, classification and clustering examples and to test algorithms. 

Similarly to the intent that Fisher had for the data, data models have been generated for machine learning where measurement data has been provided as an input, in order to predict the Iris species as an output.

![](PNG/IRIS_Image.png)



# 2. Software Requirements 

* Operating System: Windows 10.
* Python (version 3.8) via Anaconda Individual Edition Installer
* Visual Studio Code (verion 1.55.2)
* GitHub
* Pandas
* Matplotlib
* Seaborn 


**Python**

Python is known as a powerful programming language, which was originally created by Guido van Rossum in late 1980, with its first release in 1991. Python has efficient high-level data structures and a simple but effective approach to object-orientated programming. It is an interpreted language, meaning that the code can be run as soon as it written. Due to the simple syntax, Python is a popular choice for beginner programmers and has several applications such as web development, machine learning, data analysis, scripting, game development and embedded application development.[[3]](https://beginnersbook.com/2018/01/introduction-to-python-programming/) 

**Visual Studio Code**

Visual Studio Code (VS Code) is a source-code editor created by Microsoft, available on Windows, Linux and MacOS platforms. The application supports source code debugging, intelligent code completion, code snipping and embedded Git functionality to track code changes. VS Code also provides for the installation of extensions for added functionality and enhanced customization of the application for the user. 

**GitHub**

GitHub is a web-based version control and collaboration platform for software developers. The platform is based on Git, which is an open source code management system developed by Linus Torvalds (Linux Operating system creator). Its purpose is to store the source code for a project within one or more repositories, provide full traceability and complete history of all the changes to that code. GitHub is very useful for several developers collaborating together on a project and the management of any potential conflicting changes which may occur across the development team. 


**Pandas**

Pandas is an open source software library package developed for the Python programming language for analysis and manipulation of data. Pandas works perfectly well for data stored in a spreadsheet or database in a tabular form such as a comma separated values (csv), JavaScript Object Notation (JSON) and Structured Query Language (SQL) and Microsoft Excel. This type of data is referred to as a dataframe in pandas. [[4]](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)


**Matplotlib**

Matplotlib is a plotting library created for the Python programming language, with a similar design to MATLAB and utilises Numpy, the numerical extension of Python. It allows for quick visualization of data from Python by allowing various plot types to be built such as bar plot, box plot, histogram, pie chart and scatterplot. Matplotlib is included within the Anaconda installer package. 


**Seaborn** 

Seaborn is a Python data visualization library based on matplotlib, consisting of a high-level interface for creating informative statistical graphics. Seaborn is known to work well with Pandas dataframes. 



# 3. Analysis of the Dataset

Exploratory Data Analysis (EDA) is referred to as the understanding of the dataset by summarizing the main characteristics and plotting the data visually.  This is usually the first step in data analysis and will often assist in defining/verifying the problem statement or the definition on our data set.[[5]](https://medium.com/@atanudan/exploratory-data-analysis-eda-in-python-893f963cc0c0) EDA was performed using pandas to load the dataset and gather statistical information, then Matploblib and Seaborn was used to generate the various plots and identify patterns across the data.  

**Basic Information** 
  
Firstly, basic descriptive information was obtained about the dataset such as determining the dataframe dimensionality, number of rows associated with each variable, displaying a sample of the data and the data types included within the dataset. A summary information table was also generated using the info function from the pandas library and null value check was performed. This analysis verified that the loading and interpretation of the dataset was successful in the pandas package, as the dataframe dimensionality and the summary table verified the presence of 150 rows with 5 columns. 4 columns contained the sepal and petal length and width measurements, which were identified as a float data type. The final column was characterized as an object datatype as it consisted of the 3 species of Iris. The count function filtered by species showing that the dataset contained equal quantities of sample data across the 3 species, showing 50 rows for each of the Iris species. The null value check confirmed that no null values were present within the dataset. One row of values was identified as a duplicated from the virginica species. The duplicate row was not removed from the dataset, this was to ensure that the data was not imbalanced for the virgicina species and to avoid mis-interpretation of the dataset. This action is taken more often larger datasets. 
[[6]](https://towardsdatascience.com/exploratory-data-analysis-in-python-c9a77dfa39ce)


**Statistical Characteristics**

The statistical information was gathered with the use of the describe function, which provided the following details: count, mean, standard deviations, minimum values and maximum values. 
From analysis of the data in the table, larger mean values are shown are the petal and sepal lengths in comparison to the corresponding width values. 


# 4. Visualization of the Dataset 

**Histograms** 

The matplotlib histograms generated demonstrates the attribute data across the 3 species. From viewing the histogram set, it is clearly evident that the measurement values for the Versicolor and Virginica are more aligned to each other than that of the setosa species. Also, it appears that there is greater variation across the petal measurements in comparison to the sepal measurements which display a more aligned distribution throughout the species. This differentiation in measurement across the dataset indicates for the potential to identify a particular species, or at least the elimination of one species, based on the information generated from the histogram set. 

For the Seaborn generated histograms, which displays overlap between species, similar trends can be seen. Looking at species in regards to sepal length, there is a considerable level of overlap and as such would not assist in the classification problem. Likewise, with the sepal width, this displays even further overlapping. However in contrast, the petal measurements display less of an overlap for the veriscolor and viriginica species, with the setosa species displaying good separation from the other species. Therefore, petal length and petal width would be considered as more promising features to make a assess the prediction of a species when input data is provided.


**Boxplot**

The analysis from the Boxplots, is displaying the setosa species having smaller measurement values with less distribution, with the versicolor remaining the average of all the species. The virginica is showing the highest distribution across the group for the measurement values. 


**Correlations**

Based on the output for data correlation, it is easily apparent that values generated for the petal length and petal width are the most correlated on the heatmap, showing a value of r=0.96, showing a strong linear relationship. However, with the sepal length and sepal width features only displaying a slight correlation with each other.


**Scatterplot** 

From analysis of the scatterplots displaying sepal length vs sepal width, it can be seen that the Setosa species consists of a smaller sepal length but a larger width. For the versicolor, the sepal length lies in the middle in comparison to the others, as the virginica contain the largest sepal lengths, with smaller sepal widths.  

In contrast for the petal length vs petal width, the setosa species displays the small petal length and width, similar to the sepal measurements, the versicolor species again lies in the middle of the species, with an average petal length and width. Likewise, the virginica species have the largest petal measurements. 


**Pairplot** 

On viewing of the pairplot set, a high correlation can be identifed between the petal length and petal width measurements. Similar to the indications in the scatterplot, setosa is showing lower petal length and width values with the sepal width measurements higher and lenght having lower values.
For the versicolor species again, this is displaying average petal and sepal measurements. As for virginica, same trend is identified here with larger measurements for petal dimensions and smaller values associated with sepal width and larger values for sepal length.   


# 5. Conclusion 

The Iris dataset is considered to be a well-known classification problem. From the results generated as part of this project and from the extensive resources available online, applying Exploratory Data Analysis through the python programming language, demonstrates its importance and signifance as a powerful data science method in assisting with predicting a particular species when input data is available. 
The power of EDA is supported by the data manipulation and visualization packages, such as pandas, matplotlib and seaborn.

Additional analysis for machine learning will be applied through the SciKit-learn library for python at a later stage for this dataset.  


# 6. References 

**README.md References**


[1] https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-anderson36-2 \
[2] https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 \
[3] https://beginnersbook.com/2018/01/introduction-to-python-programming/ \
[4] https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html \
[5] https://medium.com/@atanudan/exploratory-data-analysis-eda-in-python-893f963cc0c0 \
[6] https://towardsdatascience.com/exploratory-data-analysis-in-python-c9a77dfa39ce 


**Source Code References**


[1] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html \
[2] https://www.geeksforgeeks.org/how-to-set-a-single-main-title-for-all-the-subplots-in-matplotlib/ \
[3] https://stackoverflow.com/questions/28638158/seaborn-facetgrid-how-to-leave-proper-space-on-top-for-suptitle \
[4] https://stackoverflow.com/questions/50259125/make-python-seaborn-heatmap-bigger 