from PIL import Image
import numpy as np

def rotate_image(image: Image.Image, angle: float) -> Image.Image:
    """Rotate the given image by a specified angle."""
    return image.rotate(angle, expand=True)

def scale_image(image: Image.Image, scale_factor: float) -> Image.Image:
    """Scale the image by a specified factor."""
    new_size = (int(image.width * scale_factor), int(image.height * scale_factor))
    return image.resize(new_size, Image.ANTIALIAS)

def adjust_brightness(image: Image.Image, factor: float) -> Image.Image:
    """Adjust the brightness of the image by a specified factor."""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image: Image.Image, factor: float) -> Image.Image:
    """Adjust the contrast of the image by a specified factor."""
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def apply_color_transform(image: Image.Image, color_matrix: np.ndarray) -> Image.Image:
    """Apply a color transformation to the image using a color matrix."""
    return image.convert("RGB", color_matrix)

def flip_image(image: Image.Image, direction: str) -> Image.Image:
    """Flip the image in the specified direction ('horizontal' or 'vertical')."""
    if direction == 'horizontal':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    elif direction == 'vertical':
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("Direction must be 'horizontal' or 'vertical'.")