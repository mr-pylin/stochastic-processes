# Random walk: https://en.wikipedia.org/wiki/Random_walk

# dependencies
import matplotlib.pyplot as plt
import numpy as np

# random 1-dimensional walking
time = 20000

# probabilities in the format of [forward, stay, backward]
probabilities = [
    [.4, .2, .4], [.05, .9, .05], [.5, 0, .5],  # same probability for 'forward' & 'backward'       [varying 'stay']
    [.6, .1, .3], [.9, 0., .1], [.2, .75, .05],  # 'forward'  has higher probability than 'backward' [varying 'stay']
    [.3, .1, .6], [.1, 0., .9], [.05, .75, .2],  # 'backward' has higher probability than 'forward'  [varying 'stay']
]

# initial location is 0 for all of the experiments for the probabilities
locations = np.zeros(shape=(len(probabilities), time))

# change the state in each time lapse
for i in range(1, time):
    for e in range(len(probabilities)):
        locations[e, i] = locations[e, i - 1] + np.random.choice([+1, 0, -1], p=probabilities[e])


# plot
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(12, 10), layout='constrained')
fig.suptitle("[p, q, r] = [forward, stay, backward] probabilities")

for row in range(3):
    for col in range(3):
        axs[row, col].hist(locations[(row * 3 + col)], bins=100)
        axs[row, col].set_title(str(probabilities[(row * 3 + col)]))

plt.show()
