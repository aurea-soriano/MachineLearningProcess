
import numpy as np
import pandas as pd

#mtcars dataset source: Henderson and Velleman (1981), Building multiple regression models interactively. Biometrics, 37, 391–411.

cars = pd.read_csv('../dataset/mtcars.csv')
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
print(cars.head())
