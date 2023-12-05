from qiskit import *
from qiskit.visualization import plot_histogram

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circ = QuantumCircuit(qr, cr)

circ.h(0)
circ.cx(0, 1)
circ.measure(qr, cr)
circ.draw(output = 'mpl', filename = 'bell.png')

sim = Aer.get_backend('qasm_simulator')
res = execute(circ, backend = sim, shots = 1000).result()
plot_histogram(res.get_counts()).savefig('bell_sim.png')
