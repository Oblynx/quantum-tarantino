import numpy as np
import matplotlib.pyplot as plt
import dimod
import networkx as nx
import sys
import time

## Time durations:
# num_reads = 100
# 10 qubits:  9.12s
# 20 qubits:  31.69s
# 100 qubits: 777.96s

start = time.time()
"""
# Crate random matrices for benchmarking
N = 100
h = {}
keys = range(N)
for i in keys:
    h[i] = 10
J = {}

for i in keys:
	for j in range(i+1,N):
		J[(i,j)] = -1.
"""

vote_weight = 1000. 
neg_vote = -1 # First Choice
pos_vote = +1 # Seconda Choice
#h = {0: neg_vote*vote_weight, 1: 0., 2: 0., 3: 0., 4: pos_vote*vote_weight, 5:0., 6:0.}
#h = {0: neg_vote*vote_weight, 1: 0., 2: 0., 3: 0., 4: 0., 5:pos_vote*vote_weight,6: 0.}

h = {0:pos_vote*vote_weight, 1: neg_vote*vote_weight, 2: neg_vote*vote_weight, 3: 0., 4: 0., 5:pos_vote*vote_weight ,6: 0.}

J = {(0, 1): -30.0, (0,2):-20.,(0,3):-50.,(0,4):-20.,(0,5):-60.,(0,6):-60.,
 		(1,2): -10.,(1,3):-20.,(1,4):-20.,(1,5):-10.,(1,6):-20.0,
 			(2,3):-60.,(2,4):-20.,(2,5):-70.,(2,6):-50.,
 				(3,4):-40.,(3,5):-70.,(3,6):-30.,
 					(4,5):-30.,(4,6):-30.,
 						(5,6):-50.
 					}

model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)
sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=1000)

pos = 0.
neg = 0.
tie = 0.
for solution in response.data():
	votes = solution.sample.values()
	if sum(votes) < 0: # Note that it works with reverse sign
		#print('Positive vote wins with: ' + str(votes))
		pos += 1.
	elif sum(votes) > 0:
		#print('Negative vote wins with: ' + str(votes))
		neg += 1.
	else:
		#print('It is a tie!')
		tie +=1.
print('Tendancy towards the First Choice is: ' + str(neg/(neg+pos+tie)))

duration = time.time() - start
print(duration)

"""
G = nx.DiGraph()
G.add_nodes_from(h.keys())

for v,k in J.items():
	G.add_edges_from([v], weight=k)
	G.add_edges_from([tuple(reversed(v))], weight=k)

plt.axis('off') 
nx.draw(G, with_labels=True) 		
#plt.show()	
plt.savefig('graph.png', format="PNG")
"""
