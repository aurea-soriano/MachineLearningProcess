'''
The dataset
We analyze the Concrete Compressive Strength Data Set from UCI ML repository in this notebook.

Abstract: Concrete is the most important material in civil engineering. The concrete compressive strength is a highly nonlinear function of age and ingredients. Can we predict the strength from other measurement values?

Data Set Information:
Number of instances: 1030
Number of Attributes: 9
Attribute breakdown 8 quantitative input variables, and 1 quantitative output variable
Missing Attribute Values: None
'''

#Import the libraries and read the data in
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

# The dataset path may be different in your situation. Please use the correct path
df = pd.read_excel(../datasets/Concrete_Data.xls")
df.head(10)

df.describe().T


#Taking a peek at the relationship between the predicting variables and the response¶
for c in df.columns[:-1]:
    plt.figure(figsize=(8,5))
    plt.title("{} vs. \nConcrete Compressive Strength".format(c),fontsize=16)
    plt.scatter(x=df[c],y=df['Concrete compressive strength(MPa, megapascals) '],color='blue',edgecolor='k')
    plt.grid(True)
    plt.xlabel(c,fontsize=14)
    plt.ylabel('Concrete compressive strength\n(MPa, megapascals)',fontsize=14)
    plt.show()


#Creating a copy with suitable column names for processing with statsmodels.OLS()

df1 = df.copy()
df1.columns=['Component'+str(i) for i in range(1,8)]+['Age']+['y']
df1.head()


#Pairwise scatter plots
from seaborn import pairplot
pairplot(df1)


#Correlation matrix and heatmap to visually check for multicollinearity
#In statistics, multicollinearity (also collinearity) is a phenomenon in which one predictor variable in a multiple regression model
#can be linearly predicted from the others with a substantial degree of accuracy.
corr = df1[:-1].corr()
corr


from statsmodels.graphics.correlation import plot_corr
fig=plot_corr(corr,xnames=corr.columns)
