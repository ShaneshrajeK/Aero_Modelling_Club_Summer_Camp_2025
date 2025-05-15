# Image Thresholding in OpenCV

Thresholding is a technique to segment an image by turning it into a binary image — separating objects from the background.

## 🔍 What You'll Learn
- Apply basic binary thresholding
- Use adaptive thresholding for uneven lighting
- Understand threshold types like `cv2.THRESH_BINARY`, `cv2.THRESH_OTSU`

## ✨ Key Functions Covered
- `cv2.threshold()`
- `cv2.adaptiveThreshold()`
- Threshold types like `THRESH_BINARY`, `THRESH_BINARY_INV`, etc.

## 📌 Applications
- Document scanning
- Object detection and shape analysis
- Preprocessing for contour detection


## 🔍 Comparison: Simple vs Adaptive Thresholding

| Feature                  | `simple_threshold.py`                        | `adaptive_threshold.py`                        |
| ------------------------ | -------------------------------------------- | ---------------------------------------------- |
| **Type of Thresholding** | Global thresholding                          | Adaptive thresholding                          |
| **Threshold Value**      | Fixed manually (e.g., 127)                   | Calculated per local region                    |
| **Function Used**        | `cv2.threshold()`                            | `cv2.adaptiveThreshold()`                      |
| **Best Use Case**        | Images with uniform lighting                 | Images with varying illumination               |
| **Advantages**           | Simple and fast                              | Better results under uneven lighting           |
| **Disadvantages**        | Sensitive to lighting variations             | Slightly slower; parameters require tuning     |
| **Example Outcome**      | Might miss edges in darker or brighter areas | Preserves edges and details across all regions |

### 📝 Summary

* Use **Simple Thresholding** when the lighting in your image is consistent.
* Use **Adaptive Thresholding** when your image has shadows or areas with different brightness levels.

> 💡 Tip: Always convert to grayscale before applying thresholding for best results.

---

Happy Coding! 🚀


