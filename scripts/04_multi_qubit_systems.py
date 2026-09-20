# %% [markdown]
# # 4. Multi-Qubit Systems
#
# This notebook explores circuits with more than one qubit, including
# **entanglement** — a special quantum correlation between qubits that
# has no classical equivalent.

# %% [markdown]
# ## Step 1: Import libraries

# %%
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_distribution, plot_histogram

simulator = AerSimulator()

# %% [markdown]
# ## Bell state (2-qubit entanglement)
#
# Steps: put qubit 0 into superposition with H, then use a CNOT (CX)
# gate so qubit 1's state becomes linked to qubit 0's state.

# %%
qc_bell = QuantumCircuit(2, 2)
qc_bell.h(0)
qc_bell.cx(0, 1)
qc_bell.draw("mpl")

# %%
probs_bell = Statevector(qc_bell).probabilities_dict()
print("Bell state probabilities:", probs_bell)
plot_distribution(probs_bell, title="Bell state: ideal probabilities")

# %%
qc_bell.measure([0, 1], [0, 1])
counts_bell = simulator.run(transpile(qc_bell, simulator), shots=1024).result().get_counts()
print("Bell state measurement counts:", counts_bell)
plot_histogram(counts_bell, title="Bell state: measurement results")

# %% [markdown]
# Notice you only ever see `'00'` or `'11'` — never `'01'` or `'10'`.
# The two qubits are entangled: measuring one instantly tells you the
# other's result, no matter how far apart they are.

# %% [markdown]
# ## GHZ state (3-qubit entanglement)
#
# The same idea extended to three qubits.

# %%
qc_ghz = QuantumCircuit(3, 3)
qc_ghz.h(0)
qc_ghz.cx(0, 1)
qc_ghz.cx(1, 2)
qc_ghz.draw("mpl")

# %%
probs_ghz = Statevector(qc_ghz).probabilities_dict()
print("GHZ state probabilities:", probs_ghz)
plot_distribution(probs_ghz, title="GHZ state: ideal probabilities")

# %%
qc_ghz.measure([0, 1, 2], [0, 1, 2])
counts_ghz = simulator.run(transpile(qc_ghz, simulator), shots=1024).result().get_counts()
print("GHZ state measurement counts:", counts_ghz)
plot_histogram(counts_ghz, title="GHZ state: measurement results")

# %% [markdown]
# ## Toffoli gate (CCX): a 3-qubit gate
#
# The target qubit flips only if BOTH control qubits are `1`. Here we
# set both controls to `1` with X gates first, so we expect the
# target to flip.

# %%
qc_toffoli = QuantumCircuit(3, 1)
qc_toffoli.x(0)          # control 1 = 1
qc_toffoli.x(1)          # control 2 = 1
qc_toffoli.ccx(0, 1, 2)  # target flips only if both controls are 1
qc_toffoli.draw("mpl")

# %%
probs_toffoli = Statevector(qc_toffoli).probabilities_dict()
print("Toffoli gate probabilities:", probs_toffoli)
plot_distribution(probs_toffoli, title="Toffoli gate: ideal probabilities")

# %%
qc_toffoli.measure(2, 0)
counts_toffoli = simulator.run(transpile(qc_toffoli, simulator), shots=1024).result().get_counts()
print("Toffoli gate measurement counts (target qubit):", counts_toffoli)
plot_histogram(counts_toffoli, title="Toffoli gate: target qubit result")

# %% [markdown]
# ## SWAP gate
#
# Swaps the states of two qubits. Here qubit 0 starts as `|1>` and
# qubit 1 starts as `|0>` — after the SWAP, they should trade places.

# %%
qc_swap = QuantumCircuit(2, 2)
qc_swap.x(0)         # qubit 0 = |1>, qubit 1 = |0>
qc_swap.swap(0, 1)   # after swap: qubit 0 = |0>, qubit 1 = |1>
qc_swap.draw("mpl")

# %%
probs_swap = Statevector(qc_swap).probabilities_dict()
print("SWAP gate probabilities:", probs_swap)
plot_distribution(probs_swap, title="SWAP gate: ideal probabilities")

# %%
qc_swap.measure([0, 1], [0, 1])
counts_swap = simulator.run(transpile(qc_swap, simulator), shots=1024).result().get_counts()
print("SWAP gate measurement counts:", counts_swap)
plot_histogram(counts_swap, title="SWAP gate: measurement results")
