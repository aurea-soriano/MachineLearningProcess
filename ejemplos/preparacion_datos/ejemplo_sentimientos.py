# importar nuestra biblioteca pandas
import pandas as pd

#algoritmo para vectorizar operaciones
from sklearn.feature_extraction.text import CountVectorizer

filepath_dict = {"yelp": "../../datasets/opiniones/yelp_labelledes.csv",
                "amazon": "../../datasets/opiniones/amazon_cells_labelledes.csv",
                "imdb": "../../datasets/opiniones/imdb_labelledes.csv"}



df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
    df['source'] = source
    df_list.append(df)

df = pd.concat(df_list)
print(df.head())

#1era estrategia vamos a crear un copntador de palabras

frases = ["A Victor le gusta linux", "Victor no no le gusta Tortoise"]
etiquetas = [1,0]
#countvectorizer para vectorizar operaciones
print(frases)
vectorizar  = CountVectorizer(lowercase=False)
vectorizar.fit(frases)
print(vectorizar.vocabulary_)

feature_vector = vectorizar.transform(frases).toarray()
print(feature_vector)

X = feature_vector
y = etiquetas

print(X)
print(y)
