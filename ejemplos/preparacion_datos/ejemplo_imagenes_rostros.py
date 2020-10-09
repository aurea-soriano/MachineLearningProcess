import numpy as np #paquete de operaciones matematicas
import matplotlib.pyplot as plt #paquete de graficos
#sklearn es un paqueton para machine learning
from sklearn.datasets import fetch_lfw_people # importando el metodo para cargar el conjunto de  personas
from sklearn.ensemble import RandomForestClassifier # importando el clasificador
from sklearn.model_selection import train_test_split # importando el metodo para dividir en entren. y prueba
from sklearn import metrics # importando las metricas de evaluacion
from sklearn.metrics import confusion_matrix # importando esta es una metrica de evaluacion Matriz de confusion
import seaborn as sns #paquete de graficos
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# para saber numero de fotos y el tamanho de fotos
n_samples, h, w = lfw_people.images.shape



# para machine learning usamos los pixels
X = lfw_people.data
n_features = X.shape[1]

# la etiqueta a predecir es el id de la persona
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("Tamaño total del dataset:")
print("número de fotos: %d" % n_samples)
print("número de características: %d" % n_features)
print("número de clases: %d" % n_classes)

# set up the figure
fig = plt.figure(figsize=(6, 6))  # figure size in inches
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# plot the faces: each image is 8x8 pixels
for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(lfw_people.images[i], cmap=plt.cm.binary, interpolation='nearest')

    # label the image with the target value
    ax.text(0, n_classes, str(lfw_people.target[i]))


for i in range(64):
  print(lfw_people.data[i])
