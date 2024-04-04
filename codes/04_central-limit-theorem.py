# more details about "Central limit theorem": https://en.wikipedia.org/wiki/Central_limit_theorem

# dependencies
import numpy as np
import matplotlib.pyplot as plt

# probability density function(PDF) of normal distribution
mu_normal  = 0
std_normal = 1
x_normal = np.linspace(mu_normal - 3 * std_normal, mu_normal + 3 * std_normal, 1000)
pdf_normal = 1 / (std_normal * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x_normal - mu_normal) / std_normal) ** 2)

# probability density function(PDF) of uniform distribution
low_uniform  = 0
high_uniform = 1
x_uniform = np.linspace(low_uniform, high_uniform, 1000)
pdf_uniform = np.where((x_uniform >= low_uniform) & (x_uniform <= high_uniform), 1 / (high_uniform - low_uniform), 0)

# probability density function(PDF) of exponential distribution
lambda_param = 0.5
x_exponential = np.linspace(0, 10, 1000)
pdf_exponential = lambda_param * np.exp(-lambda_param * x_exponential)

# number of samples in each sampling
n = 10

# number of samplings
s = 10000

# sampling
normal = np.random.normal(loc= mu_normal, scale= std_normal, size= (n, s))
uniform = np.random.uniform(low= low_uniform, high= high_uniform, size= (n, s))
exponential = np.random.exponential(scale= lambda_param, size= (n, s))

# mean per sample
normal_means = normal.mean(axis= 0)
exponential_means = exponential.mean(axis= 0)
uniform_means = uniform.mean(axis= 0)

# plot
fig, axs = plt.subplots(nrows= 3, ncols= 4, figsize= (16, 12), layout= 'compressed')
fig.suptitle("Central Limit Theorem")

for row, distribution in enumerate(['normal', 'uniform', 'exponential']):
    axs[row, 0].plot(eval(f"x_{distribution}"), eval(f"pdf_{distribution}"))
    axs[row, 0].set_title(f"{distribution} distribution")
    axs[row, 1].hist(eval(f"{distribution}_means[:100]"), bins= 50)
    axs[row, 1].set_title("#sampling= 100")
    axs[row, 2].hist(eval(f"{distribution}_means[:1000]"), bins= 50)
    axs[row, 2].set_title("#sampling= 1000")
    axs[row, 3].hist(eval(f"{distribution}_means"), bins= 50)
    axs[row, 3].set_title("#sampling= 10000")

plt.show()