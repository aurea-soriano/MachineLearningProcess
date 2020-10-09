#LendingClub - conecta a personas que necesitan dinero (prestatarios)
#con personas que tienen dinero(inversores)


# importar nuestros paquetes
import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#cargar nuestros datos
df = pd.read_csv("../../datasets/loan_data.csv")


print(df.head())


print("credit.policy- 1  si es que tiene el credito aprobado, 0 si no fue aprobado")
print(df['credit.policy'].value_counts())


print(df['purpose'])

df_final = pd.get_dummies(df, ['purpose'], drop_first=True)
print(df_final.head())

print(len(df_final.columns))
X = df_final[1:18]

y = df_final['credit.policy']

print(X)
print(y)
