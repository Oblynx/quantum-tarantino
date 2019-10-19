import numpy as np
import matplotlib.pyplot as plt
import dimod

h = {0: 100.0, 1: 0.0, 2: -100.0, 3: 0.}
J = {(0, 1): -10.0, (1,2): 0., (2,3):0.}

sampleset = dimod.SimulatedAnnealingSampler().sample_ising(h, J)
print(sum(sampleset.record[0][0]))