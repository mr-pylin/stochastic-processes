# Monty Hall problem: https://en.wikipedia.org/wiki/Monty_Hall_problem

# dependencies
import random

import matplotlib.pyplot as plt


def update_bars(fig, title, bars, new_title, new_values) -> None:
    for bar, new_value in zip(bars, new_values):
        bar.set_height(new_value)
    title.set_text(new_title)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.show()


def monty_hall(doors: list[str]) -> tuple[int]:

    # choosing a door: [0, 1, 2]
    player_1 = random.randint(0, 2)
    player_2 = random.randint(0, 2)

    # player 1 : if the chosen door is 'goat', switching to another door is a win
    if doors[player_1] == 'car':
        player_1_win = 0
    else:
        player_1_win = 1

    # player 2: if the chosen door is 'car', staying with the door is a win
    if doors[player_2] == 'car':
        player_2_win = 1
    else:
        player_2_win = 0

    return player_1_win, player_2_win


def main() -> None:

    # number of simulations
    num_simulations = 100000

    # initial objects behind each door
    doors = ['car', 'goat', 'goat']

    # win frequency
    player_1 = 0  # the switch guy
    player_2 = 0  # the stay guy

    # create initial bar plot
    fig, ax = plt.subplots()
    fig.suptitle('Monty-Hall Game')
    title = ax.set_title("")
    bars = ax.bar(['Player 1 [win rate]', 'Player 2 [win rate]'], [0, 0], label=['the switch guy', 'the stay guy'], color=['red', 'blue'])
    ax.set_yticks([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
    ax.legend()

    # turn on interactive mode
    plt.ion()

    # number of simulations
    for i in range(1, num_simulations + 1):

        # shuffle the doors
        random.shuffle(doors)

        # run Monty-Hall game
        wins = monty_hall(doors)
        player_1 += wins[0]
        player_2 += wins[1]

        # update bar plot
        update_bars(
            fig,
            title,
            bars,
            new_title=f"#Game: {i} | switch win ratio: {player_1 / i:2.2f} | stay win ratio: {player_2 / i:2.2f}",
            new_values=[player_1 / i, player_2 / i],
        )

    plt.ioff()
    plt.show()


if __name__ == '__main__':
    main()
