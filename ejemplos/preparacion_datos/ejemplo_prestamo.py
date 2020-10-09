"""
.. ejemplo:: Préstamos
   :plataforma: Unix, Windows, MAC
   :sinopsis: Ejemplo de Exploración a partir de datos relacionados a
   préstamos (LendingClub).
   Lending Club conecta a personas que necesitan dinero (prestatarios)
   con personas que tienen dinero (inversores).
.. autora:: Dra. Aurea Soriano <aurea.soriano@ic.unicamp.br>

"""


'''
credit.policy: 1 si el cliente cumple con los criterios de suscripción de crédito
de LendingClub.com, y 0 en caso contrario.
purpose: El propósito del préstamo (toma los valores
"credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", and "all_other").
int.rate: La tasa de interés del préstamo, como una proporción (una tasa
del 11% se almacenaría como 0,11). A los prestatarios que LendingClub.com
considera más riesgosos se les asignan tasas de interés más altas.
installment: Las cuotas mensuales adeudadas por el prestatario si el préstamo
está financiado.
log.annual.inc: El logaritmo natural de los ingresos anuales autoinformados del prestatario.
dti: La relación deuda-ingresos del prestatario (monto de la deuda dividido por los ingresos anuales).
fico: La calificación crediticia FICO del prestatario.
FICO Scores are calculated using many different pieces of credit data in your credit report.
days.with.cr.line: El número de días que el prestatario ha tenido una línea de crédito.
revol.bal: El saldo rotatorio del prestatario (monto impago al final del ciclo de facturación de la tarjeta de crédito).
revol.util: Tasa de utilización de la línea renovable del prestatario (la cantidad de la línea de crédito utilizada en relación con el crédito total disponible).
inq.last.6mths: número de consultas del prestatario por parte de los acreedores en los últimos 6 meses.
delinq.2yrs: El número de veces que el prestatario ha estado atrasado más de 30 días en un pago en los últimos 2 años.
pub.rec: el número de registros públicos despectivos del prestatario (declaraciones de quiebra, gravámenes fiscales o sentencias).
not.fully.paid: La cantidad de interés para la clasificación - si el prestatario devolvió el dinero en su totalidad o no
'''



#importando paquetes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#usamos pandas para leer el conjunto de datos
df = pd.read_csv('../datasets/loan_data.csv')

print(df.info())

print(df.describe())

print(df.head())

print("1 significa crédito aprobado, 0 significa no aprobado.")
print(df['credit.policy'].value_counts())


#Histograma de los scores de FICO por estado de credito aprobado
df[df['credit.policy']==1]['fico'].plot.hist(bins=30,alpha=0.5,color='blue', label='Credit.Policy=1')
df[df['credit.policy']==0]['fico'].plot.hist(bins=30,alpha=0.5, color='red', label='Credit.Policy=0')
plt.legend(fontsize=15)
plt.title ("Histograma del score FICO por politicas de credito aprobado o desaprobado", fontsize=16)
plt.xlabel("FICO score", fontsize=14)
plt.show()



#Presencia o ausencia de diferencia estadística de varios factores entre el estado de aprobación de crédito
sns.boxplot(x=df['credit.policy'],y=df['int.rate'])
plt.title("La tasa de interés varía entre prestatarios riesgosos y no riesgosos", fontsize=15)
plt.xlabel("Credit policy",fontsize=15)
plt.ylabel("Tasa de interes",fontsize=15)
plt.show()


sns.boxplot(x=df['credit.policy'],y=df['log.annual.inc'])
plt.title("El nivel de ingresos no hace una gran diferencia en las probabilidades de aprobación de crédito", fontsize=15)
plt.xlabel("Credit policy",fontsize=15)
plt.ylabel("Log. annual income",fontsize=15)
plt.show()


sns.boxplot(x=df['credit.policy'],y=df['days.with.cr.line'])
plt.title("Credit-approved users have a slightly higher days with credit line", fontsize=15)
plt.xlabel("Credit policy",fontsize=15)
plt.ylabel("Days with credit line",fontsize=15)
plt.show()


sns.boxplot(x=df['credit.policy'],y=df['dti'])
plt.title("Debt-to-income level does not make a big difference in credit approval odds", fontsize=15)
plt.xlabel("Credit policy",fontsize=15)
plt.ylabel("Debt-to-income ratio",fontsize=15)
plt.show()

#Countplot de préstamos por propósito, con el tono de color definido por not.fully.paid
plt.figure(figsize=(10,6))
sns.countplot(x='purpose',hue='not.fully.paid',data=df, palette='Set1')
plt.title("Bar chart of loan purpose colored by not fully paid status", fontsize=17)
plt.xlabel("Purpose", fontsize=15)
plt.show()


#Tendencia entre puntaje FICO y tasa de interés
sns.jointplot(x='fico',y='int.rate',data=df, color='purple', height=12)
plt.show()

#Implot para ver si la tendencia difiere entre la política de crédito no pagada y la política de crédito

plt.figure(figsize=(14,7))
sns.lmplot(y='int.rate',x='fico',data=df,hue='credit.policy',
           col='not.fully.paid',palette='Set1',height=6)
plt.show()


#Características categóricas
#La columna de propósito como categórica. Los transformamos usando variables ficticias para que sklearn pueda entenderlos.
df_final = pd.get_dummies(df,['purpose'],drop_first=True)
print(df_final.head())
