import cv2

# Load image in grayscale
img = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found. Please place 'sample.jpg' in this folder.")
    exit()

# Apply simple thresholding
_, thresh_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, thresh_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# Display
cv2.imshow("Original", img)
cv2.imshow("Binary Threshold", thresh_binary)
cv2.imshow("Binary Inverted", thresh_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()

