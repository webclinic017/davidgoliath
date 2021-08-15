import investpy as iv
import datetime as dt
import pandas as pd


def convert_date(date):
    return date.strftime("%d/%m/%Y")


def get_economic_calendar():
    '''
    countries = ['united states', 'united kingdom', 'australia', 'canada',
                 'switzerland', 'germany', 'japan', 'new zealand', 'china']
    importances = ['high', 'medium']
    today = dt.date.today()
    # get entire month (month have??? day)
    week_ago = (today + dt.timedelta(days=6))
    # print(today, week_ago)
    df = iv.economic_calendar(time_zone='GMT +7:00', time_filter='time_only',
                              countries=countries, importances=importances,
                              categories=None, from_date=convert_date(today),
                              to_date=convert_date(week_ago))
    df.to_csv('investpy/calendar/economic_calendar.csv')
    '''
    df = pd.read_csv('investpy/calendar/economic_calendar.csv', index_col=0)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    print(df)
    pass


get_economic_calendar()
