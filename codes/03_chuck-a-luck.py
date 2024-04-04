# more details about "Chuck a luck": https://en.wikipedia.org/wiki/Chuck-a-luck

# dependencies
import numpy as np

# rules
# -1 (you lose 1 dollar): no die matches the number
# +1 (you win  1 dollar): one die matches the number
# +2 (you win  2 dollar): two dice match the number
# +3 (you win  3 dollar): three dice match the number
scores = np.array([-1, 1, 2, 3])

# number of days playing this game
days = 7

# number of plays per day
t = 10000

# number on dice to match: 1
n = 1

for day in range(days):

    # simulation of playing 10000 games per day
    plays = np.random.randint(low= 1, high= 7, size= (t, 3))
    result = scores[np.sum(plays == 1, axis= 1)]

    print(f"day {day + 1} -> the owner won {-result.sum()}$ in {t} matches [on average {-result.mean()}$ per match]")
