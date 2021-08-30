'''
# main for stocks
http://theautomatic.net/2019/04/17/how-to-get-options-data-with-python/
# improve futures contract in lib
'''
from yahoo_fin import options
import datetime


def main():
    '''
    # chain = options.get_options_chain("nflx", 'August 13, 2021')
    # calls = options.get_calls("nflx", "August 20, 2021")
    puts = options.get_puts("nflx", "August 20, 2021")
    print(type(puts))   # pandas.core.frame.DataFrame
    '''
    nflx_dates = options.get_expiration_dates("nflx")
    # print(type(nflx_dates))
    info = {}
    for date in nflx_dates:
        info[date] = options.get_options_chain("nflx")
    print(info["August 13, 2021"])


if __name__ == '__main__':
    main()
