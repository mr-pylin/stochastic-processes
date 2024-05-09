# Assumptions
# 1. all participants bet before starting the match
# 2. odds are fixed
# 3. entrance per user: 5$

# Note: odds are computed as (1 / prior_probabilities)

# Example:
# prior = [.4, .4, .2]
# number of bets on each state = [40, 40, 20]
# winners are those who have bet on [1, 0, 0]
# so .4 * 2.5 * 5 * coeff = 400 (instead of 500 which means 1$ profit per bet)
# coeff = 4/5

import matplotlib.pyplot as plt
import numpy as np

num_games = 10
input_money = 5    # 5$
num_participants_per_game = 100

profit_per_bet = 1 # 1$
coeff = (input_money - profit_per_bet) / input_money

num_tests = 10000
earned_money_per_test = np.zeros(shape= num_tests)
avg_earned_money_per_test = np.zeros(shape= num_tests)

winners = losers = 0

fig, ax = plt.subplots()

for i in range(num_tests):

    # prior probabilities for each game as [A(win), tie, B(win)]
    prior_per_game = np.random.dirichlet(np.ones(3), size= num_games)

    # odds [coefficients] for each result
    odds_per_game = (1 / prior_per_game) * coeff

    # money collected from participants before starting the match
    deposit_money = num_games * num_participants_per_game * input_money

    # true winners
    result_per_game = np.zeros(shape= num_games, dtype= np.int8)

    for j, game in enumerate(prior_per_game):

        # participants bet
        participants_bet = np.random.choice([0, 1, 2], size= num_participants_per_game, p= prior_per_game[0])
        participants_bet_per_result = np.bincount(participants_bet, minlength= 3)

        # final result for each match
        result = np.random.choice([0, 1, 2], p= game)
        result_per_game[j] = result

        # give money to the winners
        deposit_money -= odds_per_game[j][result] * input_money * participants_bet_per_result[result]

        # save winners and losers
        winners += participants_bet_per_result[result]
        losers  += (num_participants_per_game - participants_bet_per_result[result])

    # update money
    earned_money_per_test[i] = deposit_money
    avg_earned_money_per_test[i] = earned_money_per_test[:i+1].mean()

    # plot
    # ax.clear()
    # ax.plot(range(i+1), avg_earned_money_per_test[:i+1])
    # ax.axhline(0, color='green', linewidth= 1)
    # plt.pause(1e-9)

# log
print(f"Winning gamblers: {winners}/{num_participants_per_game * num_games * num_tests}")
print(f"Losing  gamblers: {losers}/{num_participants_per_game * num_games * num_tests}")
print('-' * 50)
print(f"Recieved money      : {num_games * num_participants_per_game * num_tests * input_money} $")
print(f"Lost money          : {num_games * num_participants_per_game * num_tests * input_money - earned_money_per_test.sum()} $")
print(f"Profit/Loss         : {earned_money_per_test.sum()} $")
print(f"Profit/Loss per bet : {earned_money_per_test.sum() / (num_games * num_participants_per_game * num_tests)} $")

# plt.show()