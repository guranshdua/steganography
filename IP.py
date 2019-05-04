import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.util import view_as_blocks
import getpass

# Read Image
img = cv2.imread('C:/Users/Guransh/PycharmProjects/123/2.jpg')

pas = input("Enter the encryption key")
tex = input("Enter the Text to be hidden")

# Convert Image to Black and White
imgbw = color.rgb2gray(img)
print(imgbw)

# Get the height and Width of the image
height = np.size(img, 0)
width = np.size(img, 1)

# Make List of the tuple of image
# limg=list(img)

# Make blocks of the Image array
block_shape = (2, 2)  # Block Size
view = view_as_blocks(imgbw, block_shape)  # Convert into Blocks
print(view)


view[0][0][0][0]  # To acces elements
# Make Changes Here


print(view);
flatten_view = view.reshape(view.shape[0], view.shape[1], -1)
print(flatten_view.shape)



# Convert blocks back into a single array
final_image = view.transpose(0,2,1,3).reshape(-1,view.shape[1]*view.shape[3])

# Plotting the final result
imgplot = plt.imshow(final_image, cmap="gray")
plt.show()
