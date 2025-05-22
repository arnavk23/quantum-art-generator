from qiskit import QuantumCircuit
import numpy as np

def generate_random_state(num_qubits):
    """Generate a random quantum state for the given number of qubits."""
    state_vector = np.random.rand(2 ** num_qubits)
    state_vector /= np.linalg.norm(state_vector)  # Normalize the state vector
    return state_vector

def encode_classical_data(data, num_qubits):
    """Encode classical data into quantum bits."""
    if len(data) > 2 ** num_qubits:
        raise ValueError("Data exceeds the capacity of the quantum state.")
    
    # Create a quantum circuit with the specified number of qubits
    circuit = QuantumCircuit(num_qubits)
    
    # Encode data into the quantum circuit
    for i, value in enumerate(data):
        if value == 1:
            circuit.x(i)  # Apply X gate to set the qubit to |1>
    
    return circuit

def measure_circuit(circuit):
    """Measure the quantum circuit and return the results."""
    circuit.measure_all()
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=1024)
    result = job.result()
    counts = result.get_counts(circuit)
    return counts

def apply_gate(circuit, gate_name, qubit_index):
    """Apply a specified quantum gate to a given qubit in the circuit."""
    if gate_name == 'H':
        circuit.h(qubit_index)  # Apply Hadamard gate
    elif gate_name == 'X':
        circuit.x(qubit_index)  # Apply Pauli-X gate
    elif gate_name == 'Y':
        circuit.y(qubit_index)  # Apply Pauli-Y gate
    elif gate_name == 'Z':
        circuit.z(qubit_index)  # Apply Pauli-Z gate
    else:
        raise ValueError(f"Gate '{gate_name}' is not recognized.")
