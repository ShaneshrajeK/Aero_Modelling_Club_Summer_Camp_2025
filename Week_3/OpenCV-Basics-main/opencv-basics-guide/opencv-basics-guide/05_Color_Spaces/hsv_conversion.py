# Convert to HSV

import cv2

# Load an image
img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found. Please place 'sample.jpg' in this directory.")
    exit()

# Convert from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display original and HSV image
cv2.imshow("Original (BGR)", img)
cv2.imshow("HSV", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()
