# from sklearn.linear_model import LogisticRegression
# from sklego.meta import Thresholder
import random
from statistics import mean

total_risk = 40
days = 20


def calc_return(winrange=(0.7, 0.8), percent=0.02, days=20):
    total_return = 1
    for month in range(1, 13, 1):
        winrate = random.uniform(winrange[0], winrange[1])
        status = [choice_rr([0, 1], [1-winrate, winrate]) for _ in range(days)]
        windays = status.count(1)
        risk_rewards = [choice_rr() for _ in range(windays)]
        # print(windays, winrate, risk_rewards)
        multiply = 1
        for rr in risk_rewards:
            win_ = 1 + percent*rr
            multiply *= win_
        for _ in range(days-windays):
            lose_ = 1 - percent
            multiply *= lose_
        print(f'month {month}: {round(multiply, 2)}')
        total_return *= multiply
    print(f'Total return: {round(total_return, 2)}')


def choice_rr(args=[2, 2.5, 3], weight=[0.75, 0.15, 0.1]):
    rr = random.choices(args, weights=weight)
    return rr[0]


# for _ in range(10):
#     percent = total_risk/(days*100)
#     calc_return(winrange=(0.7, 0.9), percent=percent)
percent = total_risk/(days*100)
calc_return(winrange=(0.6, 0.8), percent=percent)
