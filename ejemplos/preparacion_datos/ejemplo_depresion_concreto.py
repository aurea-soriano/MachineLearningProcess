import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Read the dataset
df = pd.read_csv("../datasets/slump_test.csv",sep=',')

df.drop('No',axis=1,inplace=True)
df.head()

df.shape
