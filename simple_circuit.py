import pennylane as qml
from pennylane import numpy as np

# Create a device (simulator)
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.state()

print(circuit())