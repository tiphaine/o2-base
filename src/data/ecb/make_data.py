import os
import pandas as pd

from ecb import source_config
from utils import write_excel_file


def make_forex_euros():
    """
    Formats worldwide forex to euros data by country (source ECB). Reads the
    information location and outputs in the `source_config.py` file.
    """
    print('>> Handling latest "EUROPEAN CENTRAL BANK / forex to euros" data')
    raw_forex_eur_file = source_config.forex_data_files['latest']['raw']
    forex_eur_processed_dir = source_config.forex_data_files['latest'][
        'processed']
    forex_eur_data_raw = pd.read_csv(raw_forex_eur_file)

    for currency in [curr for curr in
                     forex_eur_data_raw.columns if
                     curr not in 'Date' and not curr.startswith('Unnamed')]:
        forex_eur_data_list = [
            ['currency', 'indicator_type', 'year', 'month', 'day',
             'indicator_value']]
        for _, row in forex_eur_data_raw.iterrows():
            date_raw = row['Date']
            date_tokens = date_raw.split('-')
            date_year = date_tokens[0]
            date_month = date_tokens[1]
            date_day = date_tokens[2]
            forex_currency = row[currency]
            forex_eur_data_list.append(
                [currency, 'forex_eur_{}'.format(currency.lower()), date_year,
                 date_month, date_day, forex_currency])
        forex_eur_data = pd.DataFrame(forex_eur_data_list[1:],
                                      columns=forex_eur_data_list[0])
        write_excel_file(forex_eur_data, os.path.join(
            forex_eur_processed_dir,
            'forex_eur_{}.xls'.format(currency.lower())))
