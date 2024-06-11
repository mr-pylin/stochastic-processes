# Markov chain: https://en.wikipedia.org/wiki/Markov_chain

# There is a mouse in the house! The mouse moves in such a way that in each room,
# it chooses one of the adjacent rooms (each with the same probability) and runs there
# (the movements occur at times n = 1, 2, ...).

# dependencies
import numpy as np

# total states to examine
n = 100

# containers for P & PI
P = np.zeros(shape=(n + 1, 4, 4))
PI = np.zeros(shape=(n + 1, 4))

# initial values
P[0] = np.array([
    [0, .5, 0, .5],
    [.5, 0, .5, 0],
    [0, .5, 0, .5],
    [.5, 0, .5, 0],
])
PI[0] = np.array([.1, .2, .3, .4])

# compute P[n] & PI[n]
for i in range(n):
    PI[i + 1] = np.matmul(P[i], PI[0])
    P[i + 1] = np.matmul(P[i], P[0])

# log
for i, pi in enumerate(PI):
    print(f"pi_{i:<3} = {PI[i]}")
