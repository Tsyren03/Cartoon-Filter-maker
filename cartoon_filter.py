import cv2
import numpy as np


def render_high_contrast_pen(image_path, output_path="cartoon.jpg"):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image at {image_path}. Check the file path.")
        return

    # 1 Base color smoothing
    color = img.copy()
    for _ in range(4):
        color = cv2.bilateralFilter(color, d=9, sigmaColor=75, sigmaSpace=75)

    # 2 Generate Pen Edges using Dodge Blend
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_inv = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(gray_inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)

    # Invert the sketch so lines are white and background is black
    darkness = 255 - sketch
    # Multiply the intensity of the lines 10x darker
    darker_sketch = cv2.convertScaleAbs(darkness, alpha=10, beta=0)
    # Invert back to black lines on a white background
    sketch = 255 - darker_sketch

    sketch_color = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

    # 3 Combine the cartoon color base with the high-contrast pencil sketch
    cartoon = (color.astype(np.float32) * sketch_color.astype(np.float32) / 255.0)
    cartoon = np.clip(cartoon, 0, 255).astype(np.uint8)

    # 4 Save the result
    cv2.imwrite(output_path, cartoon)
    print(f"Success! New image saved to your folder as: {output_path}")

    # 5. Display the result on screen
    combined = np.hstack((img, cartoon))
    h, w = combined.shape[:2]
    if w > 1920:
        combined = cv2.resize(combined, (w // 2, h // 2))

    cv2.imshow("Original vs High Contrast Pen", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    render_high_contrast_pen('image.jpg', 'my_final_cartoon.jpg')
