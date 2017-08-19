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

    # plot_data(df)

    # plot_selected(normalize_data(df), currencies, start_date, end_date)

    # global_statistics(df)

    plot_bollinger_bands(df, 'BTC_LTC')


def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band


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


def plot_bollinger_bands(df, currency):
    values = df[currency]
    window = 20

    rm = values.rolling(window=window, center=False).mean()

    rstd = values.rolling(window=window, center=False).std()

    upper_band, lower_band = get_bollinger_bands(rm, rstd)

    # Plot raw SPY values, rolling mean and Bollinger Bands
    ax = values.plot(title="Bollinger Bands", label=currency)
    rm.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.savefig('bbands.jpg')


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
