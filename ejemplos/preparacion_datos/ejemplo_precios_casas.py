#Import packages and dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../datasets/USA_Housing.csv")
df.head()


#Check basic info on the data set¶
#'info()' method to check the data types and number


df.info(verbose=True)

#describe()' method to get the statistical summary of the various features of the data set
#A percentile (or a centile) is a measure used in statistics indicating the value below which a given percentage of observations in a group of observations falls.
df.describe(percentiles=[0.1,0.25,0.5,0.75,0.9])



#'columns' method to get the names of the columns (features)
df.columns


#Basic plotting and visualization on the data set
#Pairplots using seaborn

sns.pairplot(df)


#Distribution of price (the predicted quantity)
df['Price'].plot.hist(bins=25,figsize=(8,4))

df['Price'].plot.density()



#Correlation matrix and heatmap

df.corr()

plt.figure(figsize=(10,7))
sns.heatmap(df.corr(),annot=True,linewidths=2)



#Feature and variable sets
#Make a list of data frame column names

l_column = list(df.columns) # Making a list out of column names
len_feature = len(l_column) # Length of column vector list
l_column

#Put all the numerical features in X and Price in y, ignore Address which is string for linear regression

X = df[l_column[0:len_feature-2]]
y = df[l_column[len_feature-2]]
print("Feature set size:",X.shape)
print("Variable set size:",y.shape)
Feature set size: (5000, 5)
Variable set size: (5000,)
X.head()
y.head()
