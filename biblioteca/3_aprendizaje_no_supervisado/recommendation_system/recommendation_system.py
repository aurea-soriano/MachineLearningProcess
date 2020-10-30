import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
import sklearn
from sklearn.decomposition import TruncatedSVD
from sklearn.neighbors import NearestNeighbors

book = pd.read_csv('BX-Books.csv', sep=';', error_bad_lines=False, encoding="latin-1")
book.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
user = pd.read_csv('BX-Users.csv', sep=';', error_bad_lines=False, encoding="latin-1")
user.columns = ['userID', 'Location', 'Age']
rating = pd.read_csv('BX-Book-Ratings.csv', sep=';', error_bad_lines=False, encoding="latin-1")
rating.columns = ['userID', 'ISBN', 'bookRating']

#print(rating.head())
#print(user.head())
#print(book.head())


combine_book_rating = pd.merge(rating, book, on='ISBN')
columns = ['yearOfPublication', 'publisher', 'bookAuthor', 'imageUrlS', 'imageUrlM', 'imageUrlL']
combine_book_rating = combine_book_rating.drop(columns, axis=1)
print(combine_book_rating.head())

combine_book_rating = combine_book_rating.dropna(axis = 0, subset = ['bookTitle'])

book_ratingCount = (combine_book_rating.
     groupby(by = ['bookTitle'])['bookRating'].
     count().
     reset_index().
     rename(columns = {'bookRating': 'totalRatingCount'})
     [['bookTitle', 'totalRatingCount']]
    )

rating_with_totalRatingCount = combine_book_rating.merge(book_ratingCount, left_on = 'bookTitle', right_on = 'bookTitle', how = 'left')
print(rating_with_totalRatingCount.head())


pd.set_option('display.float_format', lambda x: '%.3f' % x)
print(book_ratingCount['totalRatingCount'].describe())

# Alrededor de 1% de los libros tiene 50 calificaciones,
#el 2% tiene 29 calificaciones.
#debido a que tenemos tantos libros en nuestras bases de datos
#vamos a limitar al 1% superior, lo que nos dara un numero menor de libros
#alrededor de 3mil libros
popularity_threshold = 50
rating_popular_book = rating_with_totalRatingCount.query('totalRatingCount >= @popularity_threshold')
print(rating_popular_book.head())


#Filtering to peruvian users only
combined = rating_popular_book.merge(user, left_on = 'userID', right_on = 'userID', how = 'left')

peru_user_rating = combined[combined['Location'].str.contains("peru")]
peru_user_rating=peru_user_rating.drop('Age', axis=1)
print(peru_user_rating.head())
print(peru_user_rating.size)

peru_user_rating_pivot = peru_user_rating.pivot(index = 'bookTitle', columns = 'userID', values = 'bookRating').fillna(0)
peru_user_rating_matrix = csr_matrix(peru_user_rating_pivot.values)

# una de las distancias mas usadas es la de cosine
model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
model_knn.fit(peru_user_rating_matrix)

query_index = np.random.choice(peru_user_rating_pivot.shape[0])
distances, indices = model_knn.kneighbors(peru_user_rating_pivot.iloc[query_index, :].values.reshape(1, -1), n_neighbors = 10)


for i in range(0, len(distances.flatten())):
    if i == 0:
        print("Recomendacion para {0}:\n".format(peru_user_rating_pivot.index[query_index]))
    else:
         print('{0}: {1},con  distancia de {2}:'.format(i, peru_user_rating_pivot.index[indices.flatten()[i]], distances.flatten()[i]))


import sklearn
from sklearn.decomposition import TruncatedSVD

peru_user_rating_pivot2 = peru_user_rating.pivot(index = 'userID', columns = 'bookTitle', values = 'bookRating').fillna(0)
X = peru_user_rating_pivot2.values.T

SVD = TruncatedSVD(n_components=7, random_state=17)
matrix = SVD.fit_transform(X)
print(matrix.shape)

import warnings
warnings.filterwarnings("ignore",category =RuntimeWarning)
corr = np.corrcoef(matrix)
print(corr.shape)

peru_book_title = peru_user_rating_pivot2.columns
peru_book_list = list(peru_book_title)
coffey_hands = peru_book_list.index("The Cottage")
print(coffey_hands)


corr_coffey_hands  = corr[coffey_hands]
print(list(peru_book_title[(corr_coffey_hands<1.0) & (corr_coffey_hands>0.6)]))
