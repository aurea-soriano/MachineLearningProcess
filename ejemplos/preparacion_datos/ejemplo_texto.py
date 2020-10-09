import pandas as pd

filepath_dict = {'yelp':   '../datasets/opiniones/yelp_labelledes.csv',
                 'amazon': '../datasets/opiniones/amazon_cells_labelledes.csv',
                 'imdb':   '../datasets/opiniones/imdb_labelledes.csv'}

df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
    df['source'] = source  # Add another column filled with the source name
    df_list.append(df)

df = pd.concat(df_list)
print(df.iloc[0])


#Con este conjunto de datos, puede entrenar un modelo
#para predecir el sentimiento de una oración.


#Una forma en que podría hacer esto es contar la frecuencia
#de cada palabra en cada oración y vincular esta cuenta al conjunto
#completo de palabras en el conjunto de datos. Comenzaría tomando
#los datos y creando un vocabulario de todas las palabras en todas las
#oraciones. La colección de textos se denomina corpus en PLN.

'''
El vocabulario en este caso es una lista de palabras que aparecieron
en nuestro texto donde cada palabra tiene su propio índice. Esto
le permite crear un vector para una oración. Luego tomaría la oración
que desea vectorizar y cuenta su ocurrencia en el vocabulario. El vector
resultante será el vocabulario y un conteo para cada palabra en el vocabulario.

El vector resultante también se llama vector de características. En
un vector de características, cada dimensión puede ser una característica
numérica o categórica, como por ejemplo la altura de un edificio, el precio
de una acción o, en nuestro caso, el conteo de una palabra en un vocabulario.
Estos vectores de características son una pieza crucial en ciencia de datos
y el aprendizaje automático, ya que el modelo que desea entrenar depende de ellos.
'''


#Vamos a ilustrar esto. Imagine que tiene las siguientes dos oraciones:

sentences = ['A Juan le gusta el chocolate', 'Juan odia el chocolate']
#A continuación, puede usar CountVectorizer proporcionado por la biblioteca scikit-learn para vectorizar oraciones.

#Toma las palabras de cada oración y crea un vocabulario de todas las palabras únicas en las oraciones. Este vocabulario se puede usar para crear un vector de características del conteo de las palabras:

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=0, lowercase=False)
vectorizer.fit(sentences)
print(vectorizer.vocabulary_)

'''
Este vocabulario sirve también como un índice de cada palabra.
Ahora, puede tomar cada oración y obtener las palabras que aparecen
de acuerdo con el vocabulario anterior. El vocabulario consta de
las cinco palabras en nuestras oraciones, cada una representa una
palabra en el vocabulario. Cuando tome las dos oraciones anteriores
y las transforme con CountVectorizer obtendrá un vector que representa
el conteo de cada palabra de la oración:
'''


feature_vector = vectorizer.transform(sentences).toarray()
print(feature_vector)


from sklearn.model_selection import train_test_split

df_yelp = df[df['source'] == 'yelp']

sentences = df_yelp['sentence'].values
y = df_yelp['label'].values

print(sentences)
print(y)


from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorizer.fit(sentences)

print(vectorizer.vocabulary_)

X = vectorizer.transform(sentences).toarray()
print(X)
