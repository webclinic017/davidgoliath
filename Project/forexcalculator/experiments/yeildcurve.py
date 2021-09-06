from math import pow
import matplotlib.pyplot as plt
import numpy as np


class Zero:
    def __init__(self, maturity):
        self.maturity = maturity

    def zero_ytm(self, price):
        return pow(100/price, 1/self.maturity)-1

    def price(self, ytm):
        return 100/pow(1+ytm, self.maturity)


# periods
maturities = [2, 5, 10, 30]

# yield
# https://www.bloomberg.com/markets/rates-bonds/government-bonds/us
yields = [0.0018, 0.0069, 0.0122, 0.0189]

bonds = [Zero(i) for i in maturities]
prices = [bonds[i].price(yields[i]) for i in range(len(yields))]
print(prices)

maturities.pop(2)
marketYield = yields.pop(2)
marketPrice = prices.pop(2)
print(marketPrice, marketYield)

# because pop 10Y so interp at 10
interpolatedPrice = np.interp(10, maturities, prices)
interpolatedYeild = np.interp(10, maturities, yields)

print(interpolatedPrice, interpolatedYeild)
print(bonds[2].price(interpolatedYeild))

'''
# show graph
plt.plot(maturities, yields)
plt.show()
'''
