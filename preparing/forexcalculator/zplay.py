# from sklearn.linear_model import LogisticRegression
# from sklego.meta import Thresholder
import random
from statistics import mean

# total_risk = 12.5
# total_risk = 6.25
total_risk = 10
week_num = 4
day_num = 20
week_day = 5
rr = 2.5
min_win = 3
max_win = 4
months = 12
'''
win_day = [random.choice([4, 5], [0.75, 0.25]) for _ in range(week_num)]
win_day = [random.choice([4, 5]) for _ in range(week_num)]
'''


def test1():
    win_day = [random.randint(min_win, 5) for _ in range(week_num)]
    # print(win_day)

    # monthly return
    return_ = 1
    win_ret = 1 + (total_risk/day_num*rr)/100
    lose_ret = 1 - (total_risk/day_num)/100

    for item in win_day:
        return_ *= win_ret**item*lose_ret**(week_day-item)
        # print(return_)

    print(f'Total return 1: {return_**12}')


def test2():
    total_ret = 1
    mean_win = []
    for i in range(12):
        win_day = [random.randint(min_win, 5) for _ in range(week_num)]
        rr = random.choice([2, 2.5, 2.75, 3, 3.25, 3.5])
        # monthly return
        return_ = 1
        # print(i, mean(win_day))

        mean_win.append(mean(win_day))
        win_ret = 1 + (total_risk/day_num*rr)/100
        lose_ret = 1 - (total_risk/day_num)/100
        for item in win_day:
            return_ *= win_ret**item*lose_ret**(week_day-item)
            # print(return_)
        total_ret *= return_
    monthly_l = int(day_num-week_num*mean(mean_win))
    print(f'monthly day lose: {monthly_l} - percent: {monthly_l/day_num*100}')
    print(f'Total return 2: {total_ret}')


def test3():
    total_ret = 1
    mean_win = []
    for i in range(months):
        win_day = [random.randint(min_win, max_win) for _ in range(week_num)]
        # monthly return
        return_ = 1
        # print(i, mean(win_day))
        mean_win.append(mean(win_day))

        for item in win_day:
            # rr = random.choice([2, 2.25, 2.5, 2.75, 3])
            rr = choice_rr()
            win_ret = 1 + (total_risk/day_num*rr)/100
            lose_ret = 1 - (total_risk/day_num)/100
            return_ *= win_ret**item*lose_ret**(week_day-item)
        print(f'month {i+1}: {round(return_, 2)}')
        total_ret *= return_
    monthly_l = int(day_num-week_num*mean(mean_win))
    print(f'Mean day lose: {monthly_l} - percent: {monthly_l/day_num*100}')
    print(f'Total return: {round(total_ret, 2)}')


def choice_rr():
    rr_main = [2, 2.25, 2.5, 2.75, 3, 3.25, 3.5,
               3.75, 4, 4.25, 4.5, 4.75, 5]
    weight_ = [0.1, 0.25, 0.175, 0.175, 0.1, 0.04,
               0.03, 0.03, 0.01, 0.01, 0.01, 0.01, 0.01]
    rr = random.choices(rr_main, weights=weight_)
    return rr[0]


# test1()
# test2()
# test4()
test3()
