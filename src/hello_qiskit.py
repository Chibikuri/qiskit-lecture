import numpy as np
import qiskit as qk
from qiskit import IBMQ, Aer
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# This is for using backend of IBM
IBMQ.load_accounts()
IBMQ.backends()

q = QuantumRegister(4, "qubit")
c = ClassicalRegister(4, "classical bit")
qc = QuantumCircuit(q, c)

# Applying Hadamard gate to qubit 0
qc.h(q[0])

# Applying Hadamard gate to qubit 1, 2, 3
for i in range(1, 4):
    qc.h(q[i])

# Applying controled-Not gate from qubit 0 to qubit 1
qc.cx(q[0], q[1])
qc.cx(q[1], q[2])

# Also you can write with for
for i in range(2, 3):
    qc.cx(q[i], q[i+1])

qc.y(q[0])
qc.u1(np.pi/2, q[2])

# Measure all qubit.(You can specify which qubit you will measure)
qc.measure(q, c)

# # Using 16 qubit machine
# backend = IBMQ.get_backend('ibmq_16_melbourne')

# Using local simulator
backend = Aer.get_backend('qasm_simulator')

# Ececute circuit shots times on a backend.
job = qk.execute(qc, backend=backend, shots=1024)

# Result of execution.
result = job.result()
count = result.get_counts(qc)

# You can see how circuit is by printing circuit.
print(qc)
print(count, "\n")

# This is Hello world challenge. If you can get correct order, tell me!
word = ''.join([list("Hello, Qiskiter!")[int(b, 2)] for b in count.keys()])
print("Your result:", word)
print("Correct answer: Hello, Qiskiter!")
