# Drawing Shapes and Text

import cv2
import numpy as np

# Create a blank image (black background)
image = np.zeros((512, 512, 3), dtype=np.uint8)

# Draw a blue line
cv2.line(image, (50, 100), (450, 100), (255, 0, 0), thickness=3)

# Draw a green rectangle
cv2.rectangle(image, (50, 150), (450, 300), (0, 255, 0), thickness=2)

# Draw a filled red circle
cv2.circle(image, (250, 400), 50, (0, 0, 255), thickness=-1)

# Add text on the image
cv2.putText(image, 'OpenCV Drawing', (70, 50), cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 255, 255), 2, cv2.LINE_AA)

# Display the image
cv2.imshow("Drawing Shapes and Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
