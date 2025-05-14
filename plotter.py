from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

def plot_quantum_output(data, title='Quantum Circuit Output', xlabel='Measurement', ylabel='Probability'):
    """
    Plots the output of a quantum circuit as a bar chart.

    Parameters:
    - data: A dictionary where keys are measurement outcomes and values are their probabilities.
    - title: Title of the plot.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    """
    outcomes = list(data.keys())
    probabilities = list(data.values())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=outcomes, y=probabilities, palette='viridis')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(0, 1)
    plt.grid(axis='y')
    plt.show()

def plot_image(image, title='Artistic Image'):
    """
    Displays an image with a title.

    Parameters:
    - image: The image to be displayed.
    - title: Title of the image.
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(image, aspect='auto')
    plt.title(title)
    plt.axis('off')
    plt.show()

def plot_image_grid(images, titles=None, cols=3):
    """
    Displays a grid of images.

    Parameters:
    - images: A list of images to be displayed.
    - titles: A list of titles for each image.
    - cols: Number of columns in the grid.
    """
    rows = len(images) // cols + (len(images) % cols > 0)
    plt.figure(figsize=(15, 5 * rows))

    for i, image in enumerate(images):
        plt.subplot(rows, cols, i + 1)
        plt.imshow(image, aspect='auto')
        if titles:
            plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()