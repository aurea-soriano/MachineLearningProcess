import numpy as np
import pandas as pd

from pandas import Series, DataFrame

bank_full = pd.read_csv('../datasets/bank_full_w_dummy_vars.csv')
print(bank_full.head())

print(bank_full.info())


X = bank_full.ix[:,(18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)].values

y = bank_full.ix[:,17].values
