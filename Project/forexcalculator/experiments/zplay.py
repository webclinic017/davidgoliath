# from sklearn.linear_model import LogisticRegression
# from sklego.meta import Thresholder
import random
from statistics import mean

total_risk, days, periods, total, base = 60, 20, 1, 1, 0.001    # 0.016

if __name__ == '__main__':
    def calc_return(winrange=(0.7, 0.8), percent=0.02):
        total_return = 1
        for month in range(1, 13, 1):
            winrate = random.uniform(winrange[0], winrange[1])
            status = [choice_rr([0, 1], [1-winrate, winrate])
                      for _ in range(days)]
            windays = status.count(1)
            risk_rewards = [choice_rr() for _ in range(windays)]
            multiply = 1
            for rr in risk_rewards:
                win_ = 1 + percent*rr
                multiply *= win_
            for _ in range(days-windays):
                lose_ = 1 - percent
                multiply *= lose_
            print(month, windays, round(winrate*100, 2),
                  risk_rewards, round(multiply, 2), sep=" === ")
            total_return *= multiply
        print(f'Yearly return: {round(total_return, 2)}')
        return total_return

    def choice_rr(args=[1.5, 2, 2.5, 3], weight=[0.2, 0.65, 0.1, 0.05]):
        rr = random.choices(args, weights=weight)
        return rr[0]

    def calc_total(total, years, base):
        for count, _ in enumerate(range(years)):
            percent = total_risk/(days*100)
            yearly_return = calc_return(winrange=(0.6, 0.8), percent=percent)
            total *= yearly_return
        total_, base_ = round(total, 2), round(base*total, 3)
        print(
            f'Total return: {total_} ~ money: {base_}')

    calc_total(total, periods, base)
