# more details about "Monty Hall problem": https://en.wikipedia.org/wiki/Monty_Hall_problem

# dependencies
import random

# monti-hall simulation
def monty_hall_simulation(num_simulations: int) -> tuple[float]:
    switch_wins = stay_wins = 0

    for _ in range(num_simulations):
        doors = ['car', 'goat', 'goat']

        # shuffle the doors
        random.shuffle(doors)

        # player's first choice
        first_choice = random.choice(doors)

        # switch the door
        if first_choice == 'goat':
            switch_wins += 1

        # do not switch the door
        elif first_choice == 'car':
            stay_wins += 1

    # calculate probabilities
    switch_win_prob = (switch_wins / num_simulations) * 100
    stay_win_prob   = (stay_wins   / num_simulations) * 100

    return (switch_win_prob, stay_win_prob)

if __name__ == '__main__':
    num_simulations = 100000
    switch_win_prob, stay_win_prob = monty_hall_simulation(num_simulations)

    print(f"number of simulations: {num_simulations} times")
    print(f"probability of winning by     switching doors : {switch_win_prob:.2f} %")
    print(f"probability of winning by not switching doors : {stay_win_prob:.2f} %")