# Central limit theorem: https://en.wikipedia.org/wiki/Central_limit_theorem

# dependencies
import matplotlib.pyplot as plt
import numpy as np


def update_hist(fig, titles, axs, patches, bins, new_values, new_title) -> None:

    for i in range(len(titles)):
        # update histogram data
        n, _ = np.histogram(new_values[i], bins=bins[i])

        # update each bar in the histogram
        for count, patch in zip(n, patches[i]):
            patch.set_height(count)

        # update title
        titles[i].set_text(new_title)

        # automatically update y-ticks based on maximum value
        max_value = max(n)
        axs[i].set_yticks(np.linspace(0, max_value, 11, dtype=np.int64))

    # Redraw the plot
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.show()


def main() -> None:

    # number of samplings
    n = 1000

    # samples per sampling
    s = 10

    normal_means = []
    exponential_means = []
    uniform_means = []

    # probability density function(PDF) of normal distribution
    mu_normal = 0
    std_normal = 1
    x_normal = np.linspace(mu_normal - 3 * std_normal, mu_normal + 3 * std_normal, 1000)
    pdf_normal = 1 / (std_normal * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x_normal - mu_normal) / std_normal) ** 2)

    # probability density function(PDF) of uniform distribution
    low_uniform = 0
    high_uniform = 1
    x_uniform = np.linspace(low_uniform, high_uniform, 1000)
    pdf_uniform = np.where((x_uniform >= low_uniform) & (x_uniform <= high_uniform), 1 / (high_uniform - low_uniform), 0)

    # probability density function(PDF) of exponential distribution
    lambda_param = 0.5
    x_exponential = np.linspace(0, 10, 1000)
    pdf_exponential = lambda_param * np.exp(-lambda_param * x_exponential)

    # create initial subplots
    plt.ion()
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(12, 6), layout='compressed')
    fig.suptitle('Central Limit Theorem')
    axs[0, 0].plot(x_normal, pdf_normal)
    axs[0, 0].set_title("normal sampling")
    axs[0, 1].plot(x_uniform, pdf_uniform)
    axs[0, 1].set_title("uniform sampling")
    axs[0, 2].plot(x_exponential, pdf_exponential)
    axs[0, 2].set_title("exponential sampling")
    _, bins_normal, patches_normal = axs[1, 0].hist(normal_means, bins=50, range=(-3, 3))
    title_normal = axs[1, 0].set_title("#sampling= 0")
    _, bins_uniform, patches_uniform = axs[1, 1].hist(uniform_means, bins=50, range=(0, 1))
    title_uniform = axs[1, 1].set_title("#sampling= 0")
    _, bins_exponential, patches_exponential = axs[1, 2].hist(exponential_means, bins=50, range=(0, 2))
    title_exponential = axs[1, 2].set_title("#sampling= 0")

    for i in range(1, n + 1):
        normal_means.append(np.random.normal(loc=mu_normal, scale=std_normal, size=(s)).mean())
        uniform_means.append(np.random.uniform(low=low_uniform, high=high_uniform, size=(s)).mean())
        exponential_means.append(np.random.exponential(scale=lambda_param, size=(s)).mean())

        # update histogram plots
        if i % 5 == 0:
            update_hist(
                fig,
                titles=[title_normal, title_uniform, title_exponential],
                axs=[axs[1, 0], axs[1, 1], axs[1, 2]],
                patches=[patches_normal, patches_uniform, patches_exponential],
                bins=[bins_normal, bins_uniform, bins_exponential],
                new_values=[normal_means, uniform_means, exponential_means],
                new_title=f"#sampling: {i}",
            )

    plt.ioff()
    plt.show()


if __name__ == '__main__':
    main()
