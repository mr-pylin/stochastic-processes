# story
#    three worlds start with 100 creatures
#    each creature can produce 0,1,2 children with specific distributions and then dies
#    we examine that after 100 generations, which world is going to be extinct

# dependencies
import matplotlib.pyplot as plt
import numpy as np

# number of initial creatures
init_creatures = 100

# distribution of the number of children per creature for each scenario
distribution_1 = np.array([0.25, 0.55, 0.2])
distribution_2 = np.array([0.2, 0.6, 0.2])
distribution_3 = np.array([0.15, 0.65, 0.2])

# save number of creatures in each generation
num_creatures_1 = np.zeros(shape=init_creatures, dtype=np.int64)
num_creatures_1[0] = init_creatures

num_creatures_2 = np.zeros(shape=init_creatures, dtype=np.int64)
num_creatures_2[0] = init_creatures

num_creatures_3 = np.zeros(shape=init_creatures, dtype=np.int64)
num_creatures_3[0] = init_creatures

# create a subplot
fig, axs = plt.subplots(nrows=1, ncols=3, layout='compressed')

# compute number of creature for some generations
for generation in range(1, init_creatures):

    # calculate number of creatures in the next generation [old generation is removed]
    num_creatures_1[generation] = np.random.choice(range(len(distribution_1)), size=num_creatures_1[generation - 1], p=distribution_1).sum()
    num_creatures_2[generation] = np.random.choice(range(len(distribution_2)), size=num_creatures_2[generation - 1], p=distribution_2).sum()
    num_creatures_3[generation] = np.random.choice(range(len(distribution_3)), size=num_creatures_3[generation - 1], p=distribution_3).sum()

    # plot
    fig.suptitle(f"initial creatures: {init_creatures} | generation: {generation}")
    for ax in fig.axes:
        ax.clear()
    axs[0].plot(num_creatures_1[:generation + 1])
    axs[0].axhline(0, color='red', linewidth=1)
    axs[0].set_title(f"D:{distribution_1} | E:{distribution_1[1] + 2 * distribution_1[2]:.2f} | #alive: {num_creatures_1[generation]}")
    axs[1].plot(num_creatures_2[:generation + 1])
    axs[1].axhline(0, color='red', linewidth=1)
    axs[1].set_title(f"D:{distribution_2} | E:{distribution_2[1] + 2 * distribution_2[2]:.2f} | #alive: {num_creatures_2[generation]}")
    axs[2].plot(num_creatures_3[:generation + 1])
    axs[2].axhline(0, color='red', linewidth=1)
    axs[2].set_title(f"D:{distribution_3} | E:{distribution_3[1] + 2 * distribution_3[2]:.2f} | #alive: {num_creatures_3[generation]}")
    plt.pause(1e-2)

# force the window to stay opened
plt.show()
