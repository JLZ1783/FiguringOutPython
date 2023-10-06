#IMPORTS
import os
import tensorflow as tf
import matplotlib as plta
from PIL import Image


# Use same preprocessing as model

#Pretrained-model.py pre process copy
IMG_SIZE = 160 # All images will be resized to 160x160

# Test a single image from file system
#We will pass only image so no label will be passed
def format_example(image):
  """
  returns an image that is reshaped to IMG_SIZE
  """
  image = tf.cast(image, tf.float32)
  image = (image/127.5) - 1
  image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
  return image

#Import image from file
img_path = './content/dog1.jpg'

img = Image.open(img_path)

processed_img = format_example(img)

# # Check if shape is as expected
# print("Test image shape:", processed_img.shape)



