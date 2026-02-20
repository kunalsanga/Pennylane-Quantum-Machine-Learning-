import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit(theta):
    qml.RX(theta, wires=0)
    qml.RY(theta, wires=1)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

theta = np.pi / 4
print("Expectation value:", circuit(theta))