from PIL import Image
import os

def load_image(image_path):
    """Load an image from the specified path."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image at {image_path} does not exist.")
    return Image.open(image_path)

def save_image(image, save_path):
    """Save an image to the specified path."""
    image.save(save_path)

def preprocess_image(image, size=(256, 256)):
    """Resize and convert the image to RGB format."""
    image = image.resize(size)
    return image.convert("RGB")

def normalize_image(image):
    """Normalize the image data to the range [0, 1]."""
    return np.array(image) / 255.0

def denormalize_image(image):
    """Denormalize the image data from the range [0, 1] to [0, 255]."""
    return (image * 255).astype(np.uint8)