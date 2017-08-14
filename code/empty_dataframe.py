#!/usr/bin/env python
import pandas as pd
import logging
import datetime
import time
from decorators import log_ts

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(')(')

@log_ts
def test_run(start_date, end_date):
    df_currency = pd.read_csv('BTC_VIA.csv', index_col="date", parse_dates=True, usecols=['date', 'close'], na_values=['nan'])
    # logger.debug(df_currency)

    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)

    df1 = df1.join(df_currency, how='inner')


def get_formatted_date(my_date):
    return time.strftime('%Y-%m-%d', time.localtime(my_date))


if __name__ == '__main__':
    end_date = datetime.datetime.now()
    start_date = end_date + datetime.timedelta(days=-10)

    test_run(get_formatted_date(start_date.timestamp()), get_formatted_date(end_date.timestamp()))
