import pandas as pd
import numpy as np



frame = pd.read_csv('../datasets/rating_final.csv')
cuisine = pd.read_csv('../datasets/chefmozcuisine.csv')

print(frame.head())


print(cuisine.head())



rating_count = pd.DataFrame(frame.groupby('placeID')['rating'].count())

rating_count.sort_values('rating', ascending=False).head()


most_rated_places = pd.DataFrame([135085, 132825, 135032, 135052, 132834], index=np.arange(5), columns=['placeID'])

summary = pd.merge(most_rated_places, cuisine, on='placeID')
summary

cuisine['Rcuisine'].describe()



import numpy as np
import pandas as pd

frame =  pd.read_csv('rating_final.csv')
cuisine = pd.read_csv('chefmozcuisine.csv')
geodata = pd.read_csv('geoplaces2.csv', encoding = 'mbcs')

frame.head()

geodata.head()

places =  geodata[['placeID', 'name']]
places.head()

cuisine.head()

rating = pd.DataFrame(frame.groupby('placeID')['rating'].mean())
rating.head()

rating['rating_count'] = pd.DataFrame(frame.groupby('placeID')['rating'].count())
rating.head()




rating.describe()



rating.sort_values('rating_count', ascending=False).head()



places[places['placeID']==135085]

cuisine[cuisine['placeID']==135085]


places_crosstab = pd.pivot_table(data=frame, values='rating', index='userID', columns='placeID')
places_crosstab.head()


Tortas_ratings = places_crosstab[135085]
Tortas_ratings[Tortas_ratings>=0]
