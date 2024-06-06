# Chuck a luck: https://en.wikipedia.org/wiki/Chuck-a-luck

# dependencies
import matplotlib.pyplot as plt
import numpy as np


def update_bars(fig, ax, title, bars, new_title, new_values) -> None:
    values = list(new_values.values())
    values[0] *= -1

    for bar, new_value in zip(bars, values):
        bar.set_height(new_value)

    limit = max(-min(values), max(values)) * 1.1
    ax.set_ylim(-limit, limit)
    ax.set_xticks(range(4))
    ax.set_xticklabels([f"$-1x{new_values[-1]}", f"$+1x{new_values[1]}", f"$+2x{new_values[2]}", f"$+3x{new_values[3]}"])
    title.set_text(new_title)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.show()


def chuck_a_luck(scores: np.ndarray, match_number: int) -> int:
    dice_values = np.random.randint(low=1, high=7, size=(3))
    return scores[np.sum(dice_values == match_number)]


def main() -> None:
    # rules
    # -1 (you lose 1 dollar): no die matches the number
    # +1 (you win  1 dollar): one die matches the number
    # +2 (you win  2 dollar): two dice match the number
    # +3 (you win  3 dollar): three dice match the number
    match_number = 1
    scores = np.array([-1, 1, 2, 3])
    freq = {-1: 0, 1: 0, 2: 0, 3: 0}

    # number of simulations
    num_simulations = 10000

    # create initial bar plot
    fig, ax = plt.subplots()
    fig.suptitle('Chuck-a-luck Game')
    title = ax.set_title("")
    bars = ax.bar(['$-1', '$+1', '$+2', '$+3'], [0, 0, 0, 0], label=['loss', 'profit', '_profit', '_profit'], color=['tab:red', 'tab:green', 'tab:green', 'tab:green'])
    ax.legend()

    # turn on interactive mode
    plt.ion()

    # number of simulations
    for i in range(1, num_simulations + 1):

        # result of the match: [-1, +1, +2, +3]
        result = chuck_a_luck(scores, match_number)
        freq[result] += 1

        # update bar plot
        update_bars(
            fig,
            ax,
            title,
            bars,
            new_title=f"#Game: {i} | profit/loss per match: ${sum([k * v for k, v in freq.items()]) / i:2.3f}",
            new_values=freq,
        )

    plt.ioff()
    plt.show()


if __name__ == '__main__':
    main()
