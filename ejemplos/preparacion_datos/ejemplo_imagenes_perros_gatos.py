#importando una libreria que nos permite tener conexion con el so.
import os #operative system
import matplotlib.pyplot as plt #biblioteca de visualizacion
import matplotlib.image as mpimg #con esta vamos a leer imagenes
import numpy as np # biblioteca de operaciones
from PIL import Image #biblioteca para cargar una imagen

folder_path = "../../datasets/images_cats_dogs/cats_and_dogs_filtered"


# vamos a acceder a la carpeta que se llama train
train_folder = os.path.join(folder_path, "train")
validation_folder = os.path.join(folder_path, "validation")


#entrando a las carpetas especificas de gatos y perros
train_dogs_folder = os.path.join(train_folder, "dogs")
train_cats_folder = os.path.join(train_folder, "cats")
validation_dogs_folder = os.path.join(validation_folder, "dogs")
validation_cats_folder = os.path.join(validation_folder, "cats")


train_dogs_names = os.listdir(train_dogs_folder)
train_dogs_names.sort()

train_cats_names = os.listdir(train_cats_folder)
train_cats_names.sort()

validation_dogs_names = os.listdir(validation_dogs_folder)
validation_dogs_names.sort()

validation_cats_names = os.listdir(validation_cats_folder)
validation_cats_names.sort()


#print(len(train_dogs_names))
#print(len(validation_dogs_names))

#print(len(train_cats_names))
#print(len(validation_cats_names))


#total_dogs = len(train_dogs_names) + len(validation_dogs_names)

#print(len(train_dogs_names)*100/total_dogs )
#print(len(validation_dogs_names)*100/total_dogs )

#para crear una carpeta nueva
#dsrp_mj_folder = os.path.join(validation_folder, "mj")
#os.mkdir(dsrp_mj_folder)

nrows = 4
ncols = 4

image_index = 0

fig = plt.gcf()
image_width = 2
image_height = 2
fig.set_size_inches(ncols*image_width, nrows*image_height)

#llamamos al so para que nos de imagenes de gatos
next_cat_pix = [os.path.join(train_cats_folder, name)
                for name in train_cats_names[0:2]]

#llamamos al so para que nos de imagenes de perros
next_dog_pix = [os.path.join(train_dogs_folder, name)
                for name in train_dogs_names[0:2]]


# i, name  in enumerate (conjunto) i-posicion name- objeto
#for i, img_path in enumerate(next_cat_pix+next_dog_pix):
#    sp = plt.subplot(nrows, ncols, i+1)
#    img = mpimg.imread(img_path)
#    plt.imshow(img)

#plt.show()

#leer una de las imagenes

cat_filename = "../../datasets/images_cats_dogs/cats_and_dogs_filtered/train/cats/cat.10.jpg"

pil_im = Image.open(cat_filename)
print(pil_im)
#plt.imshow(pil_im)
#plt.show()

#1era estrategia
#objetivo-> convertir la imagen en escala de grises y aplanarla en un vector

imagen_gris = Image.open(cat_filename).convert("L")
#plt.imshow(imagen_gris, cmap='gray', vmin=0, vmax=255)
#plt.show()

imagen_vector = np.array(imagen_gris).flatten()
#

#vamos a crear de todo el conjunto de entrenamiento de gatos
# 0 - gatos y 1 - para perro
X_cats = []
y_cats = []
for cat in os.listdir(train_cats_folder):
    cat_path = os.path.join(train_cats_folder, cat)
    imagen_gris = Image.open(cat_path).convert("L")
    imagen_vector = np.array(imagen_gris).flatten()
    X_cats.append(imagen_vector)
    y_cats.append(0)

#2da estrategia - sacar histogramas
cat_filename = "../../datasets/images_cats_dogs/cats_and_dogs_filtered/train/cats/cat.10.jpg"

pil_im = Image.open(cat_filename)
imagen_gris = Image.open(cat_filename).convert("L")
plt.hist(np.array(imagen_gris).flatten(),128)
plt.show()


#3ra estrategia - sacar momentos
#momentos  - media, desviacion estandar, varianza,

#extraer momentos

mean = np.mean(np.array(imagen_gris).flatten())
print(mean)
momentos = []
momentos.append(mean)
