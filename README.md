# Cartoon-Filter-maker
## Description
This Python program utilizes OpenCV to apply a high-contrast, hand-drawn "pen and ink" cartoon style to digital photographs. Instead of using standard edge detection which can create noisy, chaotic lines, this algorithm uses a Dodge Blend technique combined with Bilateral Filtering to create smooth color blocking overlaid with heavy, stylized ink outlines.

## Demonstrations & Limitations
### 1. Successful Conversion (Good Demo)
<img width="684" height="573" alt="big_ben" src="https://github.com/user-attachments/assets/f05c853f-12e5-4fe7-ada8-68c840dce071" />

**Analysis:** The algorithm excels when processing images with smooth surfaces, geometric shapes, and distinct, high-contrast boundaries. In this demonstration, the algorithm perfectly captured the structural outlines while keeping the flat surfaces clean, resulting in a vibrant, comic-book-style illustration. 

### 2. Unsuccessful Conversion (Bad Demo)
<img width="811" height="542" alt="trump" src="https://github.com/user-attachments/assets/33d17c63-3d5f-457d-a8c6-1f045f234420" />

**Analysis:** The cartoon feeling is not well expressed in this image due to the heavy presence of micro-textures and complex lighting. The extreme 4x multiplier on the sketch intensity caused the algorithm to treat every subtle shadow, wrinkle, and skin pore as a harsh black ink line, resulting in a cluttered and messy output rather than a clean cartoon style.

### 3. Algorithm Limitations
Based on the results, this specific rendering pipeline has notable limitations:
* **Over-sensitivity to Texture:** Because the algorithm heavily multiplies the intensity of the dodge blend to achieve thick borders, it performs poorly on highly textured subjects (like realistic faces, fur, or foliage), creating excessive "noise" in the linework.
* **Lighting Dependency:** The dodge blending technique relies entirely on pixel intensity differences. Images with poor lighting, low contrast, or heavy gradient shadows will result in fragmented or entirely missing borders.
* **Static Parameter constraints:** The blur kernel size `(21, 21)` and the ink intensity multiplier `(alpha=4)` are hardcoded. A single configuration does not scale dynamically for images of vastly different resolutions or subjects.

