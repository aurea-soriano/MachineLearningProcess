'''Data Set Information:

# From Garavan Institute
# Documentation: as given by Ross Quinlan
# 6 databases from the Garavan Institute in Sydney, Australia
# Approximately the following for each database:

** 2800 training (data) instances and 972 test instances
** Plenty of missing data
** 29 or so attributes, either Boolean or continuously-valued

# 2 additional databases, also from Ross Quinlan, are also here

** Hypothyroid.data and sick-euthyroid.data
** Quinlan believes that these databases have been corrupted
** Their format is highly similar to the other databases

# 1 more database of 9172 instances that cover 20 classes, and a related domain theory
# Another thyroid database from Stefan Aeberhard

** 3 classes, 215 instances, 5 attributes
** No missing values

# A Thyroid database suited for training ANNs

** 3 classes
** 3772 training instances, 3428 testing instances
** Includes cost data (donated by Peter Turney)
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#Read the dataset
names = 'response age sex on_thyroxine query_on_thyroxine antithyroid_medication thyroid_surgery query_hypothyroid query_hyperthyroid pregnant \
sick tumor lithium goitre TSH_measured TSH T3_measured \
T3 TT4_measured TT4 T4U_measured T4U FTI_measured FTI TBG_measured TBG'
names = names.split(' ')


df = pd.read_csv('../datasets/hypothyroid.csv',index_col=False,names=names,na_values=['?'])
df.head()



to_drop=[]
for c in df.columns:
    if 'measured' in c or 'query' in c:
        to_drop.append(c)



to_drop


to_drop.append('TBG')
df.drop(to_drop,axis=1,inplace=True)
df.head()



#Let us see the basic statistics on the dataset
df.describe().T



#Are any data points are missing? We can check it using df.isna() method
#The df.isna() method gives back a full DataFrame with Boolean values - True for data present, False for missing data. We can use sum() on that DataFrame to see and calculate the number of missing values per column.

df.isna().sum()



#We can use df.dropna() method to drop those missing rows
df.dropna(inplace=True)
df.shape



#Creating a transformation function to convert + or - responses to 1 and 0
def class_convert(response):
    if response=='hypothyroid':
        return 1
    else:
        return 0
df['response']=df['response'].apply(class_convert)
df.head()

df.columns


#Exploratory data analysis
for var in ['age','TSH','T3','TT4','T4U','FTI']:
    sns.boxplot(x='response',y=var,data=df)
    plt.show()


sns.pairplot(data=df[df.columns[1:]],diag_kws={'edgecolor':'k','bins':25},plot_kws={'edgecolor':'k'})
plt.show()


#Create dummy variables for the categorical variables
df_dummies = pd.get_dummies(data=df)
df_dummies.shape
df_dummies.sample(10)
