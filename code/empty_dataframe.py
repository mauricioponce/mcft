#!/usr/bin/env python
import pandas as pd
import logging
import datetime
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(')(')

def test_run(start_date, end_date):
    dates = pd.date_range(start_date, end_date, freq='30min')

    currencies = ['BTC_VIA', 'BTC_LTC']

    df = get_data(currencies, dates)

    #plot_data(df)

    plot_selected(normalize_data(df), currencies, start_date, end_date)

    global_statistics(df)


def global_statistics(df):
    logger.debug('mean:\n{}'.format(df.mean()))
    logger.debug('median:\n{}'.format(df.median()))
    logger.debug('std:\n{}'.format(df.std()))


def normalize_data(df):
    return df / df.ix[0,:]


def get_data(currencies, dates):
    df1 = pd.DataFrame(index=dates)
    for currency in currencies:
        df_currency = pd.read_csv('{}.csv'.format(currency), index_col="date", parse_dates=True, usecols=['date', 'close'], na_values=['nan'])
        df_currency = df_currency.rename(columns={'close': currency})
        df1 = df1.join(df_currency)
    return df1


def plot_data(df, title='prices'):
    ax = df.plot(title=title, fontsize=2)

    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.savefig('foo.jpg')

def get_formatted_date(my_date):
    return time.strftime('%Y-%m-%d', time.localtime(my_date))

def plot_selected(df, columns, start_date, end_date):
    plot_data(df.ix[start_date:end_date, columns], title='selected data')

if __name__ == '__main__':
    end_date = datetime.datetime.now()
    start_date = end_date + datetime.timedelta(days=-10)

    test_run(get_formatted_date(start_date.timestamp()), get_formatted_date(end_date.timestamp()))
