import os
import cv2

base_dir = '../datasets/images_cars_planes/v_data'
train_dir = os.path.join(base_dir, 'train')
test_dir = os.path.join(base_dir, 'test')

# Directory with our training car pictures
train_cars_dir = os.path.join(train_dir, 'cars')

# Directory with our training plane pictures
train_planes_dir = os.path.join(train_dir, 'planes')

# Directory with our test car pictures
test_cars_dir = os.path.join(test_dir, 'cars')
print(test_cars_dir)

# Directory with our test planes pictures
test_planes_dir = os.path.join(test_dir, 'planes')

train_car_fnames = os.listdir(train_cars_dir)
print(train_car_fnames[:10])

train_plane_fnames = os.listdir(train_planes_dir)
train_plane_fnames.sort()
print(train_plane_fnames[:10])

print('total training car images:', len(os.listdir(train_cars_dir)))
print('total training plane images:', len(os.listdir(train_planes_dir)))
print('total test car images:', len(os.listdir(test_cars_dir)))
print('total test plane images:', len(os.listdir(test_planes_dir)))


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
next_car_pix = [os.path.join(train_cars_dir, fname)
                for fname in train_car_fnames[pic_index-8:pic_index]]
next_plane_pix = [os.path.join(train_planes_dir, fname)
                for fname in train_plane_fnames[pic_index-8:pic_index]]

for i, img_path in enumerate(next_car_pix+next_plane_pix):
  # Set up subplot; subplot indices start at 1
  sp = plt.subplot(nrows, ncols, i + 1)
  sp.axis('Off') # Don't show axes (or gridlines)

  img = mpimg.imread(img_path)
  plt.imshow(img)

plt.show()


# reads an input image
file_name= '../datasets/images_cars_planes/v_data/train/cars/1.jpg'
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


for car in os.listdir(train_cars_dir):
    im = np.array(Image.open(os.path.join(train_cars_dir, car)).convert('L'))
    print(im.flatten())

for plane in os.listdir(train_planes_dir):
    im = np.array(Image.open(os.path.join(train_planes_dir, plane)).convert('L'))
    print(im.flatten())
