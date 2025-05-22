from PIL import Image
import os

class Renderer:
    def __init__(self, output_dir='data/output_art'):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def save_image(self, image_array, filename, format='PNG'):
        """Save the generated image to the output directory."""
        image = Image.fromarray(image_array)
        image.save(os.path.join(self.output_dir, filename), format=format)
        print(f"Image saved as {filename} in {format} format.")

    def enhance_image(self, image_array, enhancement_factor=1.5):
        """Enhance the image using contrast adjustment."""
        image = Image.fromarray(image_array)
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(enhancement_factor)
        return enhanced_image

    def render_art(self, image_array, filename, enhance=False):
        """Render the final artistic image."""
        if enhance:
            image_array = self.enhance_image(image_array)
        self.save_image(image_array, filename)

    def render_multiple_artworks(self, images, filenames, enhance=False):
        """Render multiple artworks at once."""
        for image_array, filename in zip(images, filenames):
            self.render_art(image_array, filename, enhance)
