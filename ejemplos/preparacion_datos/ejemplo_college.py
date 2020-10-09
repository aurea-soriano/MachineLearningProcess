'''

The Data
For this project we will attempt to use KMeans Clustering to cluster Universities into to two groups, Private and Public. We will use a data frame with 777 observations on the following 18 variables.

Private A factor with levels No and Yes indicating private or public university
Apps Number of applications received
Accept Number of applications accepted
Enroll Number of new students enrolled
Top10perc Pct. new students from top 10% of H.S. class
Top25perc Pct. new students from top 25% of H.S. class
F.Undergrad Number of fulltime undergraduates
P.Undergrad Number of parttime undergraduates
Outstate Out-of-state tuition
Room.Board Room and board costs
Books Estimated book costs
Personal Estimated personal spending
PhD Pct. of faculty with Ph.D.’s
Terminal Pct. of faculty with terminal degree
S.F.Ratio Student/faculty ratio
perc.alumni Pct. alumni who donate
Expend Instructional expenditure per student
Grad.Rate Graduation rate

'''


#Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Read in the College_Data file using read_csv. Figure out how to set the first column as the index.

df = pd.read_csv('../datasets/College_Data',index_col=0)


#Check the head of the data

df.head()


#Check the info() and describe() methods on the data.
df.info()


df.describe()


#Exploratory Analysis
#Create a scatterplot of Grad.Rate versus Room.Board (and their linear fit) where the points are colored by the Private column.



sns.set_style('whitegrid')
sns.lmplot('Room.Board','Grad.Rate',data=df, hue='Private',
           palette='coolwarm',size=6,aspect=1,fit_reg=True)

#Create a scatterplot of F.Undergrad versus Outstate where the points are colored by the Private column.

#The plot shows that these two feature dimensions separate out baed on the type of college

sns.set_style('whitegrid')
sns.lmplot('Outstate','F.Undergrad',data=df, hue='Private',
           palette='coolwarm',size=6,aspect=1,fit_reg=False)


#Create a boxplot of student-faculty ratio based on college type

sns.boxplot(x='Private',y='S.F.Ratio',data=df)


#Create a boxplot of percent of alumni who donate based on college type
sns.boxplot(x='Private',y='perc.alumni',data=df)


#Create a stacked histogram showing Out of State Tuition based on the Private column.

sns.set_style('darkgrid')
g = sns.FacetGrid(df,hue="Private",palette='coolwarm',size=6,aspect=2)
g = g.map(plt.hist,'Outstate',bins=20,alpha=0.7)


#Create a similar histogram for the Grad.Rate column.

sns.set_style('darkgrid')
g = sns.FacetGrid(df,hue="Private",palette='coolwarm',size=6,aspect=2)
g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)


#There seems to be a private school with a graduation rate of higher than 100%

df[df['Grad.Rate'] > 100]


#Set that school's graduation rate to 100 so it makes sense. You may get a warning not an error) when doing this operation, so use dataframe operations or just re-do the histogram visualization to make sure it actually went through.

df['Grad.Rate']['Cazenovia College'] = 100

df[df['Grad.Rate'] > 100]

sns.set_style('darkgrid')
g = sns.FacetGrid(df,hue="Private",palette='coolwarm',size=6,aspect=2)
g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)
