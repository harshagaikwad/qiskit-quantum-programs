# Quantum Computing with Qiskit

A beginner-friendly, step-by-step introduction to quantum computing using
Qiskit and IBM's Aer simulator — no IBM Quantum account needed.

Every program is written as **plain, sequential Python code** (no custom
functions/classes to learn) so that anyone with basic Python knowledge
can follow along line by line. Each circuit in every file includes:

- a **circuit diagram** (`circuit.draw("mpl")`)
- the exact **statevector probability distribution** before measurement
- a **histogram** of results after running on the simulator

Available in two matching formats:
- **`notebooks/`** — Jupyter notebooks (`.ipynb`), already run once so
  you can see every diagram and chart without re-running anything
- **`scripts/`** — the exact same code as plain `.py` files

## Contents

| # | Topic | Notebook | Script |
|---|-------|----------|--------|
| 1 | Installation check | `01_installation.ipynb` | `01_installation.py` |
| 2 | Your first quantum circuit | `02_first_quantum_circuit.ipynb` | `02_first_quantum_circuit.py` |
| 3 | Single-qubit gates (X, Y, Z, H, S, T, RX, RY, RZ) | `03_single_qubit_gates.ipynb` | `03_single_qubit_gates.py` |
| 4 | Multi-qubit systems (Bell, GHZ, Toffoli, SWAP) | `04_multi_qubit_systems.ipynb` | `04_multi_qubit_systems.py` |
| 5 | Superdense coding | `05_superdense_coding.ipynb` | `05_superdense_coding.py` |
| 6 | Quantum teleportation | `06_quantum_teleportation.ipynb` | `06_quantum_teleportation.py` |
| 7 | Deutsch-Jozsa algorithm | `07_deutsch_jozsa_algorithm.ipynb` | `07_deutsch_jozsa_algorithm.py` |
| 8 | Grover's algorithm | `08_grovers_algorithm.ipynb` | `08_grovers_algorithm.py` |
| 9 | Shor's algorithm (factors 15) | `09_shors_algorithm.ipynb` | `09_shors_algorithm.py` |

## Setup

```bash
git clone <this-repo-url>
cd quantum-computing-with-qiskit
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running

**Notebooks** (recommended for first-time learners — outputs are already
included, but you can also re-run everything yourself):
```bash
jupyter notebook notebooks/
```

**Scripts** (plain Python, same code):
```bash
python3 scripts/01_installation.py
python3 scripts/02_first_quantum_circuit.py
# ...and so on
```

## What you'll see in every file

1. **Circuit diagram** — a visual picture of the gates
2. **Statevector probability distribution** — the *exact* theoretical
   chance of each outcome, computed directly from the quantum state
   (before any randomness from measurement)
3. **Histogram** — the *actual* results from running the circuit many
   times ("shots") on IBM's Aer simulator, which should closely match
   the statevector probabilities above

Comparing 2 and 3 is a great way to build intuition for how quantum
measurement works.

## Running on real IBM Quantum hardware

Every program here runs on `AerSimulator`, IBM's free local simulator.
To run on real IBM Quantum hardware instead, install
`qiskit-ibm-runtime`, get an API token at
[quantum.ibm.com](https://quantum.ibm.com), and swap `AerSimulator()`
for a `QiskitRuntimeService` backend.

## Notes

- Written for Qiskit 2.x (`qc.if_test(...)` for classical control flow,
  `QFTGate` instead of the deprecated `QFT` class).
- No custom Python functions are used anywhere — every file is plain,
  top-to-bottom code, intentionally kept simple for beginners.
- Shor's algorithm demo factors N=15 using a small 3-qubit counting
  register; since measurement is probabilistic, re-running the last
  cell occasionally gives a different (still correct) period.

## License

MIT — free to use and adapt for teaching or learning.
