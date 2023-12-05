from qiskit import *
from qiskit.visualization import plot_histogram
from math import pi, sqrt

state0 = [1/sqrt(2), -1/sqrt(2)] #This is |-> state
state1 = [1, 0] #this is |0> state
state2 = [1/sqrt(3), sqrt(2/3)] #this is  state |a>

# What is the probability to measure 1 and 0 in the |a> state?

# Creation of our circuit
qr = QuantumRegister(3)
cr = ClassicalRegister(3)
circ = QuantumCircuit(qr, cr)

circ.initialize(state0, 0)
circ.initialize(state1, 1)
circ.initialize(state2, 2)
circ.measure(qr, cr)
circ.draw(output = 'mpl', filename = 'init_circ.png')

sim = Aer.get_backend('qasm_simulator')
res = execute(circ, backend = sim, shots = 1000).result()
plot_histogram(res.get_counts(circ)).savefig('init_sim.png') 
