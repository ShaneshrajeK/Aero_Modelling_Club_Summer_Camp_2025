# Grayscale, Blur, and Edge Detection

import cv2

# Load image
img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found. Please place 'sample.jpg' in the current folder.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (7, 7), 0)

# Perform Canny edge detection
edges = cv2.Canny(blur, 50, 150)

# Display results
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blurred", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
