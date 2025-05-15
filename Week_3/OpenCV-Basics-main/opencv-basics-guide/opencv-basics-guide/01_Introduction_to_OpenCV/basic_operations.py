# Basic OpenCV Operations

import cv2
import numpy as np

# Read the image (Add your image by replacing sample.jpg)
image = cv2.imread("sample.jpg")

# Check if image was loaded properly
if image is None:
    print("Image not found. Make sure 'sample.jpg' exists in the directory.")
    exit()

# Display image properties
print("Image Shape:", image.shape)  # (height, width, channels)
print("Image Size:", image.size)    # Total number of pixels
print("Image Data Type:", image.dtype)

# Show the image
cv2.imshow("Original Image", image)

# Wait for key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image to a new file
cv2.imwrite("saved_output.jpg", image)
