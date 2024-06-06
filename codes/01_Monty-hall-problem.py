# Monty Hall problem: https://en.wikipedia.org/wiki/Monty_Hall_problem

# dependencies
import random
import matplotlib.pyplot as plt


# initial objects behind each door
doors = ['car', 'goat', 'goat']

# create a figure to plot a bar chart
fig, ax = plt.subplots()
plt.suptitle('Monty-Hall Game')


def monty_hall_simulation(num_simulations: int) -> None:

    # frequency for winning for each player
    player_1_wins = 0  # the switch guy
    player_2_wins = 0  # the stay guy

    for i in range(1, num_simulations + 1):

        # shuffle the doors
        random.shuffle(doors)

        # choosing a door: [0, 1, 2]
        player_1 = random.randint(0, 2)
        player_2 = random.randint(0, 2)

        # player 1: if the chosen door is 'goat', switching to another door is a win
        if doors[player_1] == 'goat':
            player_1_wins += 1

        # player 2: if the chosen door is 'car', staying with the door is a win
        if doors[player_2] == 'car':
            player_2_wins += 1

        # plot
        ax.clear()
        ax.set_title(f"#Game: {i} | switch win ratio: {player_1_wins / i:2.2f} | stay win ratio: {player_2_wins / i:2.2f}")
        ax.bar(['Player 1', 'Player 2'], [player_1_wins / i, player_2_wins / i], label=['wins for player 1', 'wins for player 2'], color=['red', 'blue'])
        ax.set_yticks([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
        ax.legend()
        plt.pause(0.03)


if __name__ == '__main__':
    num_simulations = 100000
    monty_hall_simulation(num_simulations)
    plt.show()
