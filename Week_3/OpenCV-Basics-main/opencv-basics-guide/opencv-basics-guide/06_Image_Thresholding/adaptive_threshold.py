import cv2

# Load image in grayscale
img = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found. Please place 'sample.jpg' in this folder.")
    exit()

# Apply Gaussian blur for noise reduction
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Apply adaptive thresholding
adaptive_mean = cv2.adaptiveThreshold(blur, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 11, 2)

adaptive_gaussian = cv2.adaptiveThreshold(blur, 255,
                                          cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 11, 2)

# Display
cv2.imshow("Original", img)
cv2.imshow("Adaptive Mean", adaptive_mean)
cv2.imshow("Adaptive Gaussian", adaptive_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
