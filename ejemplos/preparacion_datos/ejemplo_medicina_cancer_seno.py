#Import libraries and load data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Get the Data
#We'll use the built in breast cancer dataset from Scikit Learn. Note the load function:


from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
#The data set is presented in a dictionary form

cancer.keys()

#We can grab information and arrays out of this dictionary to create data frame and understand the features

#The description of features are as follows
print(cancer['DESCR'])


'''
:Attribute Information:
        - radius (mean of distances from center to points on the perimeter)
        - texture (standard deviation of gray-scale values)
        - perimeter
        - area
        - smoothness (local variation in radius lengths)
        - compactness (perimeter^2 / area - 1.0)
        - concavity (severity of concave portions of the contour)
        - concave points (number of concave portions of the contour)
        - symmetry
        - fractal dimension ("coastline approximation" - 1)
        '''

#Show the feature names

cancer['feature_names']

df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df.info()

df.describe()


#Is there any missing data?

np.sum(pd.isnull(df).sum()) # Sum of the count of null objects in all columns of data frame


#What are the 'target' data in the data set?

cancer['target']


#Adding the target data to the DataFrame

df['Cancer'] = pd.DataFrame(cancer['target'])
df.head()


#Exploratory Data Analysis
#Check the relative counts of benign (0) vs malignant (1) cases of cancer
sns.set_style('whitegrid')
sns.countplot(x='Cancer',data=df,palette='RdBu_r')


#Run a 'for' loop to draw boxlots of all the mean features (first 10 columns) for '0' and '1' CANCER OUTCOME
l=list(df.columns[0:10])
for i in range(len(l)-1):
    sns.boxplot(x='Cancer',y=l[i], data=df, palette='winter')
    plt.figure()


#Not all the features seperate out the cancer predictions equally clearly
#For example, from the following two plots it is clear that smaller area generally is indicative of positive cancer detection, while nothing concrete can be said from the plot of mean smoothness

f,(ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(12,6))
ax1.scatter(df['mean area'],df['Cancer'])
ax1.set_title("Cancer cases as a function of mean area", fontsize=15)
ax2.scatter(df['mean smoothness'],df['Cancer'])
ax2.set_title("Cancer cases as a function of mean smoothness", fontsize=15)
