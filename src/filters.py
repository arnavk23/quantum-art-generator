from scipy.ndimage import gaussian_filter
import cv2
import numpy as np

def apply_gaussian_blur(image, sigma=1):
    """
    Apply Gaussian blur to an image.

    Parameters:
    - image: Input image as a NumPy array.
    - sigma: Standard deviation for Gaussian kernel.

    Returns:
    - Blurred image as a NumPy array.
    """
    return gaussian_filter(image, sigma=sigma)

def apply_edge_detection(image):
    """
    Apply edge detection to an image using the Canny method.

    Parameters:
    - image: Input image as a NumPy array.

    Returns:
    - Edges detected in the image as a NumPy array.
    """
    return cv2.Canny(image, 100, 200)

def normalize_image(image):
    """
    Normalize the image to the range [0, 1].

    Parameters:
    - image: Input image as a NumPy array.

    Returns:
    - Normalized image as a NumPy array.
    """
    return (image - np.min(image)) / (np.max(image) - np.min(image))

def enhance_contrast(image, clip_limit=0.03):
    """
    Enhance the contrast of an image using CLAHE (Contrast Limited Adaptive Histogram Equalization).

    Parameters:
    - image: Input image as a NumPy array.
    - clip_limit: Threshold for contrast limiting.

    Returns:
    - Contrast-enhanced image as a NumPy array.
    """
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(8, 8))
    return clahe.apply((image * 255).astype(np.uint8)) / 255.0

def apply_filter(image, filter_type='blur', **kwargs):
    """
    Apply a specified filter to the image.

    Parameters:
    - image: Input image as a NumPy array.
    - filter_type: Type of filter to apply ('blur', 'edge').
    - kwargs: Additional parameters for the filter functions.

    Returns:
    - Processed image as a NumPy array.
    """
    if filter_type == 'blur':
        return apply_gaussian_blur(image, **kwargs)
    elif filter_type == 'edge':
        return apply_edge_detection(image)
    else:
        raise ValueError("Unsupported filter type. Use 'blur' or 'edge'.")
