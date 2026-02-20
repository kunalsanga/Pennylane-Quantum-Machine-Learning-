import pennylane as qml
from pennylane import numpy as np
from sklearn.datasets import make_moons

# Create toy dataset
X, y = make_moons(n_samples=100, noise=0.1)
y = 2*y - 1  # Convert labels to -1, 1

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit(weights, x):
    qml.RX(x[0], wires=0)
    qml.RY(x[1], wires=1)
    qml.CNOT(wires=[0,1])
    qml.RX(weights[0], wires=0)
    qml.RY(weights[1], wires=1)
    return qml.expval(qml.PauliZ(0))

def loss(weights):
    preds = np.array([circuit(weights, x) for x in X])
    return np.mean((preds - y)**2)

weights = np.random.randn(2, requires_grad=True)
opt = qml.GradientDescentOptimizer(stepsize=0.1)

for i in range(50):
    weights = opt.step(loss, weights)
    if i % 10 == 0:
        print(f"Step {i}, Loss: {loss(weights)}")

print("Final weights:", weights)

# Run circuit once to generate tape
_ = circuit(weights, X[0])

tape = circuit._tape  # internal tape

print("\nCircuit operations:")
ops = tape.operations
print(ops)

print("Total gates:", len(ops))

cnot_count = sum(1 for op in ops if op.name == "CNOT")
print("CNOT gates:", cnot_count)

print("Circuit depth:", tape.graph._depth)