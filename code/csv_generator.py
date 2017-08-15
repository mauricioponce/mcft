#!/usr/bin/env python
from poloniex import Poloniex
import sys
import datetime
import time
import logging
import csv

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(')(')

polo = Poloniex()

def get_data(currency_pair, start_date, end_date, period):
    chart_data = polo.returnChartData(currency_pair, period, start_date, end_date)
    return chart_data


def generate_csv(currency_pair, start_date, end_date, period=1800):
    data = get_data(currency_pair, start_date, end_date, period)
    filename = currency_pair + '.csv'
    logger.debug(filename)

    with open(filename, 'w') as fp:
        my_writer = csv.writer(fp, delimiter=',')
        rows = []
        keys = data[0].keys()
        my_writer.writerow([k for k in keys])
        for d in data:
            row = [d[x] for x in keys]
            row[0] = get_formatted_date(d['date'])
            rows.append(row)
        my_writer.writerows(rows)

    logger.info('%s file was created (:', filename)

def get_formatted_date(my_date):
    return time.strftime('%Y-%m-%d %H:%M', time.localtime(my_date))

if __name__ == '__main__':
    end_date = datetime.datetime.now()
    start_date = end_date + datetime.timedelta(days=-10)
    logger.debug(sys.argv)
    currency_pair = sys.argv[1]

    generate_csv(currency_pair, start_date, end_date)
    logger.debug('----------------------')
