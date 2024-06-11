# Assumptions
# 1. all participants bet before starting the match
# 2. odds are fixed
# 3. entrance per user: 5$

# prior = [a, b, c]
# odds  = 1 / prior    = [1/a, 1/b, 1/c]
# consider a variable "input_money"     denoted as p
# consider a variable "profit_per_bet"  denoted as n
# consider a variable "coeff"           denoted as m
# we have    : a * (1/a) * (p * m) + b * (1/b) * (p * m) + c * (1/c) * (p * m) = 3 * (p - n)
# simplified : 3 * p * m = 3 * (p - n)    ->    m = (p - n) / p

# dependencies
import matplotlib.pyplot as plt
import numpy as np

num_games = 10
input_money = 5    # 5$
num_participants_per_game = 100

profit_per_bet = 0  # 0$
coeff = (input_money - profit_per_bet) / input_money

num_tests = 50000
earned_money_per_test = np.zeros(shape=num_tests)
avg_earned_money_per_test = np.zeros(shape=num_tests)

winners = losers = 0

fig, ax = plt.subplots()

for i in range(num_tests):

    # prior probabilities for each game as [A(win), tie, B(win)]
    prior_per_game = np.random.dirichlet(np.ones(3), size=num_games)

    # odds [coefficients] for each result
    odds_per_game = (1 / prior_per_game) * coeff

    # money collected from participants before starting the match
    deposit_money = num_games * num_participants_per_game * input_money

    # true winners
    result_per_game = np.zeros(shape=num_games, dtype=np.int8)

    for j, game in enumerate(prior_per_game):

        # participants bet
        participants_bet = np.random.choice([0, 1, 2], size=num_participants_per_game, p=prior_per_game[0])
        participants_bet_per_result = np.bincount(participants_bet, minlength=3)

        # final result for each match
        result = np.random.choice([0, 1, 2], p=game)
        result_per_game[j] = result

        # give money to the winners
        deposit_money -= odds_per_game[j][result] * input_money * participants_bet_per_result[result]

        # save winners and losers
        winners += participants_bet_per_result[result]
        losers += (num_participants_per_game - participants_bet_per_result[result])

    # update money
    earned_money_per_test[i] = deposit_money
    avg_earned_money_per_test[i] = earned_money_per_test[:i+1].mean()

    # plot
    if (i+1) % 200 == 0:
        ax.clear()
        ax.plot(range(i+1), avg_earned_money_per_test[:i+1] / (num_games * num_participants_per_game))
        ax.axhline(profit_per_bet, color='green', linewidth=1)
        ax.set_title(f"profit/loss per bet: {earned_money_per_test[:i+1].sum() / (num_games * num_participants_per_game * (i+1)):.3f} $")
        plt.pause(1e-9)

# log
print(f"Winning gamblers: {winners}/{num_participants_per_game * num_games * num_tests}")
print(f"Losing  gamblers: {losers}/{num_participants_per_game * num_games * num_tests}")
print('-' * 50)
print(f"Recieved money      : {num_games * num_participants_per_game * num_tests * input_money} $")
print(f"Lost money          : {num_games * num_participants_per_game * num_tests * input_money - earned_money_per_test.sum()} $")
print(f"Profit/Loss         : {earned_money_per_test.sum()} $")
print(f"Profit/Loss per bet : {earned_money_per_test.sum() / (num_games * num_participants_per_game * num_tests)} $")

plt.show()
