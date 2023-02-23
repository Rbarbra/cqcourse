# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:05:17 2022

@author: Nassim
"""

#####################################################
# Libraries

from skimage import data

import numpy as np

import matplotlib.pyplot as plt




########################################################

camera = data.camera()

print(type(camera))


# exercise
# Create a 3*3 image which is a cross
# 9 Pixels

#img_cross = 


our_3D_cross_list = [[[0,0,0],[255,0,0],[0,0,0]],
                      [[255,255,0],[0,0,255],[0,255,255]],
                      [[0,0,0],[255,0,0],[0,0,0]]]

our_3D_cross_array = np.array(our_3D_cross_list)

plt.imshow(our_3D_cross_array)


our_2D_boolean_list = [[False, True, False],
                      [True,True,True],
                      [False, True, False]]

our_2d_boolean_array = np.asarray(our_2D_boolean_list)


plt.imshow(our_2d_boolean_array, cmap='gray')


print(our_2d_boolean_array.ndim)

print(our_3D_cross_array.ndim)

print(our_2d_boolean_array.shape)

print(our_3D_cross_array.shape)


print(camera.shape)
print(camera.size)


# Get minimum pixel value of your camera
print(camera.min())

# Get maximum pixel value of your camera
print(camera.max())

# How to calculate the mean of pixel values
print(camera.mean())


# Length ot the array
print(len(camera))

# Numpy imdexing

# Exercise > Set the pixel at the 3rd row and 3rd colum to 0 (camera)

# numpy array is also a list
# so you can change a numpy array like changing lists

plt.imshow(camera, cmap='gray')

camera[100,100] = 0

plt.imshow(camera, cmap='gray')


camera[100:120,100:120] = 0
plt.imshow(camera, cmap='gray')


######## Slicing

sliced_camera = camera[50:200]

plt.imshow(sliced_camera, cmap='gray')


########## cropping

headed_guy = camera[50:200,150:300]

plt.imshow(headed_guy, cmap='gray')


########### Masking
# A mask ist a boolean Matrix

mask = camera > 100

mask_2 = camera <= 100


camera[mask] = 255

camera[mask_2] = 0

plt.imshow(camera, cmap='gray')


#########################################################

# Lets create some images

# np.ones((a,b))  # a rows and b columns
# np.zeros((a,b)) # a rows and b columns

test_zero = np.zeros((500,500))

plt.imshow(test_zero, cmap='gray')

test_ones = np.ones((100,100))

plt.imshow(test_ones, cmap='gray')

# As we said, you can modify a numpy array as a list

# Exercise > Create a diagonal white line form tof-left to bottom-right
# 5 Minutes till 9

print(test_zero.shape)
print(test_zero.shape[0])
print(test_zero.shape[1])

for i in range(test_zero.shape[0]):
    for j in range(test_zero.shape[1]):
        if i == j:
            test_zero[i,j] = 255
    
plt.imshow(test_zero, cmap='gray')  

print(range(5))

x = range(5)

print(list(x))

y = range(100)

print(list(y))

for i in range(100):
    print(i)


my_list = [1,2,3,4] 


for i in my_list:
    print(i)
    
    
my_string = 'my name is Nassim El Masri'

    
for i in my_string:
    print(i)   

#############################################################

my_sequence = 'CGCATTAGGGGGTTGGCCCC'
my_new_sequence = ''

for i in my_sequence:
    if i == 'C':
        #my_new_sequence += 'G'
        my_new_sequence = my_new_sequence + 'G'
    else:
        #my_new_sequence += i
        my_new_sequence = my_new_sequence + i
print(my_new_sequence)


###############################################################

for i in my_sequence:
    print(i)
#############################################################

my_tuple = (1,2,3,4)

my_set = {1,2,3,4}

print(my_set)

my_new_set = {1,2,2,2,2,3,4}

print(my_new_set)


###########################################################

### colored images
cat = data.chelsea()

plt.imshow(cat)

print(type(cat))

print(cat.shape)

print(cat.ndim)

# You have now a 3 dimensional matrix
# each pixel is a small list of 3 values R,G,B

# Exercise > Change the color of the eye to red
# Red square instead of the eye
# 5 Minutes till 09:40

cropped_cat_eye = cat[75:180,120:220]

plt.imshow(cropped_cat_eye)

cat[75:180,120:220] = [255,0,0]
plt.imshow(cat)


cat = data.chelsea()
plt.imshow(cat)

reddish_cat = cat[:,:,0]

plt.imshow(reddish_cat, cmap='gray')


# Exercise
# Take the green layer of the cat and plot it as a gray image
# take the blue layer of the cat and plot it as a gray image

greenish_cat = cat[:,:,1]
bluish_cat = cat[:,:,2]

plt.imshow(greenish_cat, cmap='gray')
plt.imshow(bluish_cat, cmap='gray')

plt.imshow(cat, cmap='gray')

# 3 D Masking

reddish_mask = cat[:,:,0] > 150

print(reddish_mask)


cat[reddish_mask] = [255,0,0]

plt.imshow(cat, cmap='gray')


greenish_mask = cat[:,:,1] < 120

cat[greenish_mask] = [0,0,0]
plt.imshow(cat, cmap='gray')


#########################################
# From Fabian
# Another better way for extracting the red layer 
# The result is a 3D Image
cat = data.chelsea()
for i in range(cat.shape[0]):    
    for j in range(cat.shape[1]):        
        cat[i,j,1]=0        
        cat[i,j,2]=0
plt.imshow(cat)


##########################################


### Flattening a 2 D Array to a 1 D Array
# We need this when we plot a Histogram of the pixel values of an image

camera = data.camera()

# We have 3 options
# flat
# flatten
# ravel

camera_flat = camera.flat # Attribute

print(camera.size)

# Flat is a generator, so we need list to see what ist inside, 
# Or we can use ist directly like range for iteration

camera_flatten = camera.flatten() # Function
# Flatten is not a generator > We get directly an array

camera_ravel = camera.ravel() # function and also not a generator


# There is difference between ravel and flatten
# We will discuss this if there is time for this













