import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('../datasets/titanic_train.csv') # Training set is already available
train.head()

#Check basic info about the data set including missing value
t=train.info()

d=train.describe()
d


#Exploratory analysis and plots
#Plot a bar diagram to check the number of numeric entries

#From the bar diagram, it shows that there are some age entries missing as the number of count for 'Age' is less than the other counts. We can do some impute/transformation of the data to fill-up the missing entries.

dT=d.T
dT.plot.bar(y='count')
plt.title("Bar plot of the count of numeric features",fontsize=17)


#Check the relative size of survived and not-survived

sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train,palette='RdBu_r')


#Is there a pattern for the survivability based on sex?

#It looks like more female survived than males!

sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data=train,palette='RdBu_r')


#What about any pattern related to passenger class?

#It looks like disproportionately large number of 3rd class passengers died!

sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')


#Following code extracts and plots the fraction of passenger count that survived, by each class

f_class_survived=train.groupby('Pclass')['Survived'].mean()
f_class_survived = pd.DataFrame(f_class_survived)
f_class_survived
f_class_survived.plot.bar(y='Survived')
plt.title("Fraction of passengers survived by class",fontsize=17)



#What about any pattern related to having sibling and spouse?

#It looks like there is a weak trend that chance of survibility increased if there were more number of sibling or spouse

sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='SibSp',data=train,palette='rainbow')


#How does the overall age distribution look like?

plt.xlabel("Age of the passengers",fontsize=18)
plt.ylabel("Count",fontsize=18)
plt.title("Age histogram of the passengers",fontsize=22)
train['Age'].hist(bins=30,color='darkred',alpha=0.7,figsize=(10,6))


#How does the age distribution look like across passenger class?

#It looks like that the average age is different for three classes and it generally decreases from 1st class to 3rd class.

plt.figure(figsize=(12, 10))
plt.xlabel("Passenger Class",fontsize=18)
plt.ylabel("Age",fontsize=18)
sns.boxplot(x='Pclass',y='Age',data=train,palette='winter')


f_class_Age=train.groupby('Pclass')['Age'].mean()
f_class_Age = pd.DataFrame(f_class_Age)
f_class_Age.plot.bar(y='Age')
plt.title("Average age of passengers by class",fontsize=17)
plt.ylabel("Age (years)", fontsize=17)
plt.xlabel("Passenger class", fontsize=17)


'''
Data wrangling (impute and drop)
Impute age (by averaging)
Drop unncessary features
Convert categorical features to dummy variables
'''
#Define a function to impute (fill-up missing values) age feature

a=list(f_class_Age['Age'])

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):

        if Pclass == 1:
            return a[0]

        elif Pclass == 2:
            return a[1]

        else:
            return a[2]

    else:
        return Age


#Apply the above-defined function and plot the count of numeric features

train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)
d=train.describe()
dT=d.T
dT.plot.bar(y='count')
plt.title("Bar plot of the count of numeric features",fontsize=17)


#Drop the 'Cabin' feature and any other null value

train.drop('Cabin',axis=1,inplace=True)
train.dropna(inplace=True)
train.head()



#Drop other unnecessary features like 'PassengerId', 'Name', 'Ticket'
train.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
train.head()


#Convert categorial feature like 'Sex' and 'Embarked' to dummy variables
#Use pandas 'get_dummies()' function

sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'],drop_first=True)
#Now drop the 'Sex' and 'Embarked' columns and concatenate the new dummy variables

train.drop(['Sex','Embarked'],axis=1,inplace=True)
train = pd.concat([train,sex,embark],axis=1)
train.head()


#This data set is now ready!!!
