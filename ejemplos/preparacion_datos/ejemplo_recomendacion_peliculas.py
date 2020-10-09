import numpy as np
import pandas as pd

import sklearn
from sklearn.decomposition import TruncatedSVD

columns = ['user_id', 'item_id', 'rating', 'timestamp']
frame = pd.read_csv('../dataset/ml-100k/u.data', sep='\t', names=columns)
frame.head()


columns = ['item_id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
          'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

movies = pd.read_csv('../dataset/ml-100k/u.item', sep='|', names=columns, encoding='latin-1')
movie_names = movies[['item_id', 'movie title']]
movie_names.head()


combined_movies_data = pd.merge(frame, movie_names, on='item_id')
combined_movies_data.head()


combined_movies_data.groupby('item_id')['rating'].count().sort_values(ascending=False).head()


filter = combined_movies_data['item_id']==50
combined_movies_data[filter]['movie title'].unique()

rating_crosstab = combined_movies_data.pivot_table(values='rating', index='user_id', columns='movie title', fill_value=0)
rating_crosstab.head()


#Transposing the Matrix

rating_crosstab.shape
X = rating_crosstab.T
X.shape

#Decomposing the Matrix
SVD = TruncatedSVD(n_components=12, random_state=17)

resultant_matrix = SVD.fit_transform(X)

resultant_matrix.shape

#Generating a Correlation Matrix
corr_mat = np.corrcoef(resultant_matrix)
corr_mat.shape

#Isolating Star Wars From the Correlation Matrix
movie_names = rating_crosstab.columns
movies_list = list(movie_names)

star_wars = movies_list.index('Star Wars (1977)')
star_wars
corr_star_wars = corr_mat[1398]
corr_star_wars.shape

#Recommending a Highly Correlated Movie
list(movie_names[(corr_star_wars<1.0) & (corr_star_wars > 0.9)])
list(movie_names[(corr_star_wars<1.0) & (corr_star_wars > 0.95)])
