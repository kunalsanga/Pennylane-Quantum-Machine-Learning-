# ⚛️ PennyLane — Quantum Machine Learning

![PennyLane](https://img.shields.io/badge/PennyLane-Quantum%20ML-blueviolet?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxNiIgY3k9IjE2IiByPSIxNCIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A hands-on introduction to **Quantum Computing** and **Quantum Machine Learning** using [PennyLane](https://pennylane.ai/) — from building your first quantum circuit to training a **Variational Quantum Classifier (VQC)** on real data.

---

## 📁 Project Structure

```
PennyLane/
│
├── simple_circuit.py     # Bell state: Hadamard + CNOT entanglement
├── param_circuit.py      # Parameterized rotations + expectation values
├── vqc_train.py          # Variational Quantum Classifier on make_moons dataset
├── .gitignore
└── README.md
```

---

## 🚀 STEP 1 — Set Up a Virtual Environment

Create a fresh virtual environment to keep your dependencies isolated:

```bash
python -m venv qml-env
```

**Activate it:**

| Platform    | Command                         |
|-------------|----------------------------------|
| 🪟 Windows | `qml-env\Scripts\activate`       |
| 🍎 Mac/Linux | `source qml-env/bin/activate`  |

You should now see `(qml-env)` at the start of your terminal prompt.

---

## 📦 STEP 2 — Install Dependencies

With the virtual environment active, install the required packages:

```bash
pip install pennylane
pip install matplotlib
pip install scikit-learn
```

> 💡 **All at once (optional):**
> ```bash
> pip install pennylane matplotlib scikit-learn
> ```

---

## ✅ STEP 3 — Verify Installation

Test that PennyLane installed correctly:

```bash
python -c "import pennylane as qml; print(qml.__version__)"
```

If a version number prints (e.g., `0.38.0`) → **you're all set!** ⚡

---

## ▶️ STEP 4 — Run the Scripts

### 🔵 1. `simple_circuit.py` — Bell State Circuit

Creates a **2-qubit Bell state** using a Hadamard gate and a CNOT gate — the classic quantum entanglement circuit.

```bash
python simple_circuit.py
```

**What it does:**
- Applies `H` (Hadamard) to qubit 0 → puts it in superposition
- Applies `CNOT` with qubit 0 as control, qubit 1 as target → entangles them
- Returns the full **quantum state vector**

**Expected output:**
```
[0.70710678+0.j 0.        +0.j 0.        +0.j 0.70710678+0.j]
```

---

### 🟣 2. `param_circuit.py` — Parameterized Quantum Circuit

Demonstrates a **parameterized circuit** using rotation gates with a trainable angle `θ`.

```bash
python param_circuit.py
```

**What it does:**
- Applies `RX(θ)` to qubit 0 and `RY(θ)` to qubit 1
- Entangles them with `CNOT`
- Measures the **expectation value** of the Pauli-Z operator on qubit 0

**Expected output:**
```
Expectation value: 0.7071067811865476
```

---

### 🟡 3. `vqc_train.py` — Variational Quantum Classifier (VQC)

Trains a **Variational Quantum Classifier** on the `make_moons` dataset from scikit-learn — a real quantum machine learning example!

```bash
python vqc_train.py
```

**What it does:**
- Loads the `make_moons` dataset (100 samples, non-linearly separable)
- Encodes classical data into quantum states via `RX` / `RY` rotations
- Adds trainable weight layers (`RX`, `RY` + `CNOT`)
- Optimizes using **quantum gradient descent** (PennyLane's `GradientDescentOptimizer`)
- Runs for **50 training steps** and reports loss every 10 steps

**Expected output:**
```
Step 0,  Loss: 0.9523...
Step 10, Loss: 0.7841...
Step 20, Loss: 0.6102...
Step 30, Loss: 0.4987...
Step 40, Loss: 0.4213...
Final weights: [...]
```

> The loss decreases across steps, showing the quantum model is **learning**! 🧠

---

## 🧠 Concepts Covered

| Concept | Script |
|---------|--------|
| Quantum gates (H, CNOT, RX, RY) | `simple_circuit.py`, `param_circuit.py` |
| Quantum entanglement (Bell state) | `simple_circuit.py` |
| Parameterized quantum circuits | `param_circuit.py` |
| Expectation values (Pauli-Z) | `param_circuit.py` |
| Data encoding into qubit rotations | `vqc_train.py` |
| Quantum gradient descent | `vqc_train.py` |
| Variational Quantum Classifier | `vqc_train.py` |

---

## 🔧 Requirements

| Package | Purpose |
|---------|---------|
| `pennylane` | Quantum circuit simulation & ML |
| `scikit-learn` | `make_moons` dataset generation |
| `matplotlib` | (Optional) Plotting |
| `numpy` | Numerical operations (bundled with PennyLane) |

---

## 📚 Resources

- 📖 [PennyLane Documentation](https://docs.pennylane.ai/)
- 🎓 [PennyLane Demos & Tutorials](https://pennylane.ai/qml/)
- 🔬 [Quantum Machine Learning Paper (Biamonte et al.)](https://www.nature.com/articles/nature23474)
- 💻 [PennyLane GitHub](https://github.com/PennyLaneAI/pennylane)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">
  Made with ❤️ and ⚛️ quantum magic
</div>
