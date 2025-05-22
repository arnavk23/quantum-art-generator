from qiskit import QuantumCircuit, Aer, execute
import numpy as np

class ArtCircuit:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def apply_gate(self, gate, qubit):
        if gate == 'H':
            self.circuit.h(qubit)
        elif gate == 'X':
            self.circuit.x(qubit)
        elif gate == 'Y':
            self.circuit.y(qubit)
        elif gate == 'Z':
            self.circuit.z(qubit)
        elif gate == 'CX':
            if qubit + 1 < self.num_qubits:
                self.circuit.cx(qubit, qubit + 1)

    def initialize_circuit(self):
        for qubit in range(self.num_qubits):
            self.apply_gate('H', qubit)

    def measure(self):
        self.circuit.measure_all()

    def get_circuit(self):
        return self.circuit

    def execute_circuit(self):
        backend = Aer.get_backend('qasm_simulator')
        self.measure()
        job = execute(self.circuit, backend, shots=1024)
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def generate_artistic_pattern(self):
        self.initialize_circuit()
        return self.execute_circuit()
