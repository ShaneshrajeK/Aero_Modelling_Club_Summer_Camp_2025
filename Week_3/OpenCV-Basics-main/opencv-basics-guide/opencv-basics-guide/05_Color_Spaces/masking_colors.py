# Mask Specific Colors

import cv2
import numpy as np

# Load image
img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found. Please place 'sample.jpg' in this folder.")
    exit()

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define range for a color (e.g., blue)
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

# Create a mask
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply the mask
result = cv2.bitwise_and(img, img, mask=mask)

# Display everything
cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.imshow("Filtered Color", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
