# Record Video from Webcam

import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # or 'MJPG', 'MP4V', etc.
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Write the frame to the output file
    out.write(frame)

    # Show the live video
    cv2.imshow("Recording...", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
