# more details about "Ehrenfest model/chain": https://de.wikipedia.org/wiki/Ehrenfest-Modell

# dependencies
import numpy as np
import matplotlib.pyplot as plt

# inputs
num_of_molecules = 1000
time = 10000

# distribution 1: at the beginning (time=0), all molecules are inside the container=0
distribution_1 = np.zeros(shape= num_of_molecules)
num_of_molecules_before_1 = (int(num_of_molecules - distribution_1.sum()), int(distribution_1.sum()))
distribution_mean_per_time_1 = np.empty(shape= time)

# distribution 2: at the beginning (time=0), all molecules are inside the container=1
distribution_2 = np.ones(shape= num_of_molecules)
num_of_molecules_before_2 = (int(num_of_molecules - distribution_2.sum()), int(distribution_2.sum()))
distribution_mean_per_time_2 = np.empty(shape= time)

# distribution 3: at the beginning (time=0), molecules are spread into two containers by 50/50 chance
distribution_3 = np.zeros(shape= num_of_molecules)
distribution_3[: num_of_molecules // 2] = 1
num_of_molecules_before_3 = (int(num_of_molecules - distribution_3.sum()), int(distribution_3.sum()))
distribution_mean_per_time_3 = np.empty(shape= time)
                  
# change the state in each time lapse
for i in range(time):

    # modify distributions
    random_molecule_index_1 = np.random.choice(num_of_molecules)
    distribution_1[random_molecule_index_1] = 1 - distribution_1[random_molecule_index_1]

    random_molecule_index_2 = np.random.choice(num_of_molecules)
    distribution_2[random_molecule_index_2] = 1 - distribution_2[random_molecule_index_2]
    
    random_molecule_index_3 = np.random.choice(num_of_molecules)
    distribution_3[random_molecule_index_3] = 1 - distribution_3[random_molecule_index_3]

    # compute new mean for time=i
    distribution_mean_per_time_1[i] = np.mean(distribution_1)
    distribution_mean_per_time_2[i] = np.mean(distribution_2)
    distribution_mean_per_time_3[i] = np.mean(distribution_3)

num_of_molecules_after_1 = (int(num_of_molecules - distribution_1.sum()), int(distribution_1.sum()))
num_of_molecules_after_2 = (int(num_of_molecules - distribution_2.sum()), int(distribution_2.sum()))
num_of_molecules_after_3 = (int(num_of_molecules - distribution_3.sum()), int(distribution_3.sum()))

# plot
def show_container(i, j, **kwargs):
    axs[i, j].plot([0.5, 0.5], [0, 1], color= 'black')
    axs[i, j].set(xlim= (0, 1), ylim= (0, 1), xticks= [], yticks= [], **kwargs)

def add_text(i, j, molecules_per_container):
    axs[i, j].text(0.25, 0.5, f"molecules= {molecules_per_container[0]}", fontsize= 10, ha= 'center')
    axs[i, j].text(0.25, 0.9, "container 0", fontsize= 10, ha= 'center', color= 'red')
    axs[i, j].text(0.75, 0.5, f"molecules= {molecules_per_container[1]}", fontsize= 10, ha= 'center')
    axs[i, j].text(0.75, 0.9, "container 1", fontsize= 10, ha= 'center', color= 'red')

fig, axs = plt.subplots(nrows= 3, ncols= 3, figsize= (12, 10), layout= 'constrained')

# first row
show_container(0, 0, title= "Distribution 1 [before]")
add_text(0, 0, num_of_molecules_before_1)
show_container(0, 1, title= "Distribution 2 [before]")
add_text(0, 1, num_of_molecules_before_2)
show_container(0, 2, title= "Distribution 3 [before]")
add_text(0, 2, num_of_molecules_before_3)

# second row
axs[1, 0].hist(distribution_mean_per_time_1, bins= 50)
axs[1, 0].set(title= "Distribution of means", xticks= np.linspace(0, 1, 5))
axs[1, 1].hist(distribution_mean_per_time_2, bins= 50)
axs[1, 1].set(title= "Distribution of means", xticks= np.linspace(0, 1, 5))
axs[1, 2].hist(distribution_mean_per_time_3, bins= 50)
axs[1, 2].set(title= "Distribution of means", xticks= np.linspace(0, 1, 5))

# third row
show_container(2, 0, title= "Distribution 1 [after]")
add_text(2, 0, num_of_molecules_after_1)
show_container(2, 1, title= "Distribution 2 [after]")
add_text(2, 1, num_of_molecules_after_2)
show_container(2, 2, title= "Distribution 3 [after]")
add_text(2, 2, num_of_molecules_after_3)

plt.show()