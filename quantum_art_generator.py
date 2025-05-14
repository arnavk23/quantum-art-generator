from qiskit import QuantumCircuit, Aer, execute
import numpy as np
import matplotlib.pyplot as plt
from image_processing.filters import apply_filters
from image_processing.transformations import apply_transformations
from visualization.plotter import plot_results
from visualization.renderer import render_art
from quantum_circuits.art_circuit import ArtCircuit

class QuantumArtGenerator:
    def __init__(self, input_image_path, output_image_path):
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path
        self.art_circuit = ArtCircuit()

    def generate_art(self):
        # Step 1: Create quantum circuit for art generation
        circuit = self.art_circuit.create_art_circuit()
        
        # Step 2: Execute the circuit
        backend = Aer.get_backend('statevector_simulator')
        result = execute(circuit, backend).result()
        output_state = result.get_statevector()

        # Step 3: Process the output state to create an image
        processed_image = self.process_output(output_state)

        # Step 4: Save and render the final art
        render_art(processed_image, self.output_image_path)

    def process_output(self, output_state):
        # Convert quantum state to image data
        image_data = self.quantum_state_to_image(output_state)
        
        # Apply filters and transformations
        filtered_image = apply_filters(image_data)
        transformed_image = apply_transformations(filtered_image)

        return transformed_image

    def quantum_state_to_image(self, output_state):
        # Normalize the quantum state to create an image
        magnitude = np.abs(output_state)**2
        image_data = magnitude.reshape((int(np.sqrt(len(magnitude))), -1))
        return image_data

if __name__ == "__main__":
    input_image_path = 'data/input_images/sample_image.png'  # Example input image path
    output_image_path = 'data/output_art/generated_art.png'  # Example output image path

    art_generator = QuantumArtGenerator(input_image_path, output_image_path)
    art_generator.generate_art()