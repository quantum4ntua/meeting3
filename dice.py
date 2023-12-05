from qiskit import *
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

def greater_count(counts, keys):
    i = 0
    key_ret = '000'
    for key in keys:
        if counts[key] > i:
            i = counts[key]
            key_ret = key
    return key_ret

qr = QuantumRegister(3)
cr = ClassicalRegister(3)
circ = QuantumCircuit(qr, cr)
roll_again = False

while(roll_again is not True):
    for i in range(3):
        circ.h(i)
    circ.measure(qr, cr)
    circ.draw(output = 'mpl', filename = 'dice_circ.png')

    sim = Aer.get_backend('qasm_simulator')
    res = execute(circ, backend = sim, shots = 1000).result()
    counts = res.get_counts(circ)
    keys = list(counts.keys())
    x = greater_count(counts, keys)
    print(x)
    nums = str(x)
    num = nums[::-1]
    i = 0
    j = 0
    for a in num:
        i += int(a) * (2**j)
        j += 1

    if i > 0 and i < 7:
        print(f"My number is {i}")
        roll_again = True

    plot_histogram(counts).savefig('dice_hist.png')
