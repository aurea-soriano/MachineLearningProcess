"""
    :ejemplo: Jugadores de Futbol
    :plataforma: Unix, Windows, Mac
    :sinopsis: Ejemplo de exploracion a partir de datos rde jugadores de futbol.
    :autora: Aurea Soriano. aurea.soriano@ic.unicamp.br
"""

#Importando las bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


#leyendo los Datos
data = pd.read_csv('../../datasets/fifa_eda.csv')

print(data.sample(5))

print(data.head())

print(data.tail())

print(data.info())

print(data.describe())

print(data.isnull().any())

# llenando valores faltantes de variables continuas
data['ShortPassing'].fillna(data['ShortPassing'].mean(), inplace = True)
#data['ShortPassing'].value_counts(dropna = False)
data['Volleys'].fillna(data['Volleys'].mean(), inplace = True)
#data['Volleys'].value_counts(dropna = False)
data['Dribbling'].fillna(data['Dribbling'].mean(), inplace = True)
#data['Dribbling'].value_counts(dropna = False)
data['Curve'].fillna(data['Curve'].mean(), inplace = True)
#data['Curve'].value_counts(dropna = False)
data['FKAccuracy'].fillna(data['FKAccuracy'], inplace = True)
#data['FKAccuracy'].value_counts(dropna = False)
data['LongPassing'].fillna(data['LongPassing'].mean(), inplace = True)
#data['LongPassing'].value_counts(dropna = False)
data['BallControl'].fillna(data['BallControl'].mean(), inplace = True)
#data['BallControl'].value_counts(dropna = False)
data['HeadingAccuracy'].fillna(data['HeadingAccuracy'].mean(), inplace = True)
#data['HeadingAccuracy'].value_counts(dropna = False)
data['Finishing'].fillna(data['Finishing'].mean(), inplace = True)
#data['Finishing'].value_counts(dropna = False)
data['Crossing'].fillna(data['Crossing'].mean(), inplace = True)
#data['Crossing'].value_counts(dropna = False)
data['Weight'].fillna('200lbs', inplace = True)
data['Weight'].value_counts(dropna = False)
data['Contract Valid Until'].fillna(2019, inplace = True)
#data['Contract Valid Until'].value_counts(dropna = False)
data['Height'].fillna("5'11", inplace = True)
data['Height'].value_counts(dropna = False)



# llenando valores faltantes de variables
data['Club'].fillna('No Club', inplace = True)
data['Club'].value_counts(dropna = False)
data['Work Rate'].fillna('Medium/ Medium', inplace = True)
data['Work Rate'].value_counts(dropna = False)
data['Preferred Foot'].fillna('Right', inplace = True)
data['Preferred Foot'].value_counts(dropna = False)

# llenando valores faltantes de variables continuas
data['Skill Moves'].fillna(data['Skill Moves'].median(), inplace = True)
data['Skill Moves'].value_counts(dropna = False)
data['Weak Foot'].fillna(3, inplace = True)
data['Weak Foot'].value_counts(dropna = False)
data['International Reputation'].fillna(1, inplace = True)
data['International Reputation'].value_counts(dropna = False)


#preferencia de pierna(zurda o diestra) de los jugadores
data['Preferred Foot'].value_counts().plot.bar()

#comparando reputacion
data['International Reputation'].value_counts()

labels = ['1', '2', '3', '4', '5']
sizes = [16532, 1261, 309, 51, 6]
colors = ['red', 'yellow', 'green', 'pink', 'blue']
explode = [0.1, 0.1, 0.2, 0.5, 0.9]

plt.pie(sizes, labels = labels, colors = colors, explode = explode, shadow = True)
plt.title('Reputacion', fontsize = 25)
plt.legend()
plt.show()



# posiciones de los jugadores

plt.figure(figsize = (12, 8))
sns.set(style = 'dark', palette = 'colorblind', color_codes = True)
ax = sns.countplot('Position', data = data, color = 'orange')
ax.set_xlabel(xlabel = 'Posiciones', fontsize = 16)
ax.set_ylabel(ylabel = '# de Jugadores', fontsize = 16)
ax.set_title(label = 'Comparacion de jugadores y posiciones', fontsize = 20)
plt.show()


data['Wage'].fillna('€200K', inplace = True)
data['Wage'].isnull().any()

# definiendo una funcion para limpiar el valor del peso
def extract_value_from(value):
  out = value.replace('lbs', '')
  return float(out)

# aplicando la funcion a la columna de peso
#data['value'] = data['value'].apply(lambda x: extract_value_from(x))
data['Weight'] = data['Weight'].apply(lambda x : extract_value_from(x))

data['Weight'].head()


# aplicando la funcion a la columna de sueldo

def extract_value_from(Value):
    out = Value.replace('€', '')
    if 'M' in out:
        out = float(out.replace('M', ''))*1000000
    elif 'K' in Value:
        out = float(out.replace('K', ''))*1000
    return float(out)



# aplicando la funcion a la columna de sueldo

data['Value'] = data['Value'].apply(lambda x: extract_value_from(x))
data['Wage'] = data['Wage'].apply(lambda x: extract_value_from(x))

data['Wage'].head()

# Comparing the players' Wages

sns.set(style = 'dark', palette = 'bright', color_codes = True)
plt.figure(figsize = (75, 4))
x = data.Wage
sns.countplot(x, data = data, color = 'y')
plt.xlabel('Rango de sueldos de jugadores', fontsize = 16)
plt.ylabel('Numero de jugadoress', fontsize = 16)
plt.title('Comparando los sueldos de los jugadores', fontsize = 20)
plt.show()


data['Height'].head(10)

# Altura de los jugadores

plt.figure(figsize = (13, 8))
ax = sns.countplot(x = 'Altura', data = data, palette = 'dark')
ax.set_title(label = 'Numero de jugadores relacionados a su altura en pies', fontsize = 20)
ax.set_xlabel(xlabel = 'Altura', fontsize = 16)
ax.set_ylabel(ylabel = 'Numero de Jugadores', fontsize = 16)
plt.show()


#diferentes pesos
plt.figure(figsize = (30, 8))
sns.countplot(x = 'Weight', data = data, palette = 'dark')
plt.title('Numero de jugadores relacionados a su peso en libras en FIFA2019', fontsize = 20)
plt.xlabel('Peso', fontsize = 16)
plt.ylabel('Numero de Jugadores', fontsize = 16)
plt.show()



# nacionalidad
data['Nationality'].value_counts().plot.bar(color = 'orange', figsize = (35, 15 ))
plt.title('Diferente Nacionalidades en FIFA2019')
plt.xlabel('Nombre del Pais')
plt.ylabel('Numero de Jugadores')
plt.show()

#edad
sns.set(style = "dark", palette = "colorblind", color_codes = True)
x = data.Age
plt.figure(figsize = (12,8))
ax = sns.distplot(x, bins = 58, kde = False, color = 'g')
ax.set_xlabel(xlabel = "Edad", fontsize = 16)
ax.set_ylabel(ylabel = 'Numero de Jugadores', fontsize = 16)
ax.set_title(label = 'Histograma de la edad ', fontsize = 20)
plt.show()


print(data.columns)
# seleccionando columnas interesasntes
selected_columns = ['Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value',
                    'Wage', 'Special', 'Preferred Foot', 'International Reputation', 'Weak Foot',
                    'Skill Moves', 'Work Rate', 'Body Type', 'Position', 'Height', 'Weight',
                    'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                    'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
                    'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
                    'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
                    'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
                    'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
                    'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause']

data_selected = pd.DataFrame(data, columns = selected_columns)
print(data_selected.columns)

print(data_selected.sample(5))


#correlacion
plt.rcParams['figure.figsize'] = (30, 20)
sns.heatmap(data_selected[['Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value',
                    'Wage', 'Special', 'Preferred Foot', 'International Reputation', 'Weak Foot',
                    'Skill Moves', 'Work Rate', 'Body Type', 'Position', 'Height', 'Weight',
                    'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                    'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
                    'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
                    'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
                    'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
                    'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
                    'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause']].corr(), annot = True)

plt.title('Histogram of the Dataset', fontsize = 30)
plt.show()


# comparando desempeno de zurdos y diestros
# ballcontrol vs dribbing

sns.lmplot(x = 'BallControl', y = 'Dribbling', data = data, col = 'Preferred Foot')
