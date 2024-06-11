# story:
#    two gamblers with some wealth($), compete with each other.
#    at each round, the winner owns <fee>($) from loser.
#    the game finishes when one of the gamblers has 0$ money.

# Assumptions:
#    Gambler B has intinte money.
#    Gambler A has finite  money.
#    The game can be started with different win rates.

# dependencies
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

# set wealth & luck for both gamblers
stats = {
    'A': {'wealth': 50, 'win_rate': float(input("Gambler A's win rate (e.g. 0.5): "))},
    'B': {'wealth': float('inf'), 'win_rate': float(input("Gambler B's win rate (e.g. 0.5): "))},
}

# initial wealths shall be positive
for key, value in stats.items():
    if value['wealth'] <= 0:
        raise ValueError(f"Player {key} has an insufficient amount of money: {value['wealth']}$.")

# probabilities shall sum to 1
if stats['A']['win_rate'] + stats['B']['win_rate'] != 1:
    raise ValueError(f"sum of probabilities: {(stats['A']['win_rate'], stats['B']['win_rate'])} must equal to 1")

# amount of money in $ to win at each round
fee = 1

# create a subplot
fig, ax = plt.subplots(layout='compressed')

# This match ends when a gambler becomes bankrupt
counter = 0
gambler_A = defaultdict(int, {stats['A']['wealth']: 1})
while stats['A']['wealth'] > 0 and stats['B']['wealth'] > 0:

    # fee
    stats['A']['wealth'] -= fee
    stats['B']['wealth'] -= fee

    # win
    winner = np.random.choice(('A', 'B'), p=(stats['A']['win_rate'], stats['B']['win_rate']))
    stats[winner]['wealth'] += 2 * fee

    # capture gambler A's current wealth
    gambler_A[stats['A']['wealth']] += 1

    counter += 1

    # plot
    if counter % 10 == 0:
        ax.clear()
        ax.bar(gambler_A.keys(), gambler_A.values())
        ax.axvline(0, color='red', linewidth=2)
        ax.set_title(f"#match: {counter} | wealths: [A:{stats['A']['wealth']}, B:{stats['B']['wealth']}] | win rates: [A:{stats['A']['win_rate']}, B:{stats['B']['win_rate']}]")
        plt.pause(1e-9)

# announce the winner
if stats['A']['wealth'] == 0:
    ax.set_title(f"#match: {counter} | wealths: [A:{stats['A']['wealth']}, B:{stats['B']['wealth']}] | win rates: [A:{stats['A']['win_rate']}, B:{stats['B']['win_rate']}] | winner: B")
else:
    ax.set_title(f"#match: {counter} | wealths: [A:{stats['A']['wealth']}, B:{stats['B']['wealth']}] | win rates: [A:{stats['A']['win_rate']}, B:{stats['B']['win_rate']}] | winner: A")

# force the window to stay opened
plt.show()
