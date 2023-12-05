from qiskit import *
from qiskit.quantum_info.operators import Operator
from qiskit.visualization import plot_histogram
from math import sqrt

U = [[(1/sqrt(2)) ,(1/sqrt(2))], [1.j*(1/sqrt(2)) , -1.j*(1/sqrt(2))]]

qr = QuantumRegister(1)
cr = ClassicalRegister(1)
circ = QuantumCircuit(qr, cr)

circ.unitary(U, 0, label = 'U')
circ.measure(0, 0)
circ.draw(output = 'mpl', filename = 'new_gate.png')

sim = Aer.get_backend('qasm_simulator')
res = execute(circ, backend = sim, shots = 1000).result()
plot_histogram(res.get_counts()).savefig('new_gate_sim.png')

# Does this gate remind you of something? If yes, why?
