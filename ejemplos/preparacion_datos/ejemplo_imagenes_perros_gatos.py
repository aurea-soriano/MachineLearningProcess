import os
import cv2

base_dir = '../datasets/images_cats_dogs/cats_and_dogs_filtered'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# Directory with our training cat pictures
train_cats_dir = os.path.join(train_dir, 'cats')

# Directory with our training dog pictures
train_dogs_dir = os.path.join(train_dir, 'dogs')

# Directory with our validation cat pictures
validation_cats_dir = os.path.join(validation_dir, 'cats')
print(validation_cats_dir)

# Directory with our validation dog pictures
validation_dogs_dir = os.path.join(validation_dir, 'dogs')

train_cat_fnames = os.listdir(train_cats_dir)
print(train_cat_fnames[:10])

train_dog_fnames = os.listdir(train_dogs_dir)
train_dog_fnames.sort()
print(train_dog_fnames[:10])

print('total training cat images:', len(os.listdir(train_cats_dir)))
print('total training dog images:', len(os.listdir(train_dogs_dir)))
print('total validation cat images:', len(os.listdir(validation_cats_dir)))
print('total validation dog images:', len(os.listdir(validation_dogs_dir)))


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Parameters for our graph; we'll output images in a 4x4 configuration
nrows = 4
ncols = 4

# Index for iterating over images
pic_index = 0

# Set up matplotlib fig, and size it to fit 4x4 pics
fig = plt.gcf()
fig.set_size_inches(ncols * 4, nrows * 4)

pic_index += 8
next_cat_pix = [os.path.join(train_cats_dir, fname)
                for fname in train_cat_fnames[pic_index-8:pic_index]]
next_dog_pix = [os.path.join(train_dogs_dir, fname)
                for fname in train_dog_fnames[pic_index-8:pic_index]]

for i, img_path in enumerate(next_cat_pix+next_dog_pix):
  # Set up subplot; subplot indices start at 1
  sp = plt.subplot(nrows, ncols, i + 1)
  sp.axis('Off') # Don't show axes (or gridlines)

  img = mpimg.imread(img_path)
  plt.imshow(img)

plt.show()


# reads an input image
file_name= '../datasets/images_cats_dogs/cats_and_dogs_filtered/train/dogs/dog.0.jpg'
from PIL import Image
import numpy as np

pil_im = Image.open(file_name)
plt.imshow(pil_im)
plt.show()

# find frequency of pixels in range 0-255
im = np.array(Image.open(file_name).convert('L'))
plt.hist(im.flatten(),128)


# show the plotting graph of an image
plt.show()



pil_im = Image.open(file_name).convert('L')
plt.imshow(pil_im)
plt.show()
im = np.array(Image.open(file_name).convert('L'))
print(im.flatten())


for cat in os.listdir(train_cats_dir):
    im = np.array(Image.open(os.path.join(train_cats_dir, cat)).convert('L'))
    print(im.flatten())

for dog in os.listdir(train_dogs_dir):
    im = np.array(Image.open(os.path.join(train_dogs_dir, dog)).convert('L'))
    print(im.flatten())
