from qiskit import *
from qiskit.visualization import plot_histogram

# Creating Our Circuit

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circ = QuantumCircuit(qr, cr)

state1 = [0, 1]
circ.initialize(state1, 1) #what happens with no initialization
circ.h(0)
circ.h(1)
circ.cx(0, 1)
circ.h(0)
circ.h(1)
circ.measure(qr, cr)
circ.draw(output = 'mpl', filename = 'cnot.png')

sim = Aer.get_backend('qasm_simulator')
simsv = Aer.get_backend('statevector_simulator')
res = execute(circ, backend = sim, shots = 1000).result()
resv = execute(circ, backend = simsv, shots = 1000).result()
state = resv.get_statevector(experiment = circ)
print(state)
plot_histogram(res.get_counts()).savefig('cnot_sim.png')
