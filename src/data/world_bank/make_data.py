import numpy as np
import pandas as pd

from src.data.world_bank import source_config
from src.data.utils import write_excel_file


def make_inflation_country():
    """
    Formats worldwide inflation data by country (source World Bank). Reads the
    information location and outputs in the `source_config.py` file.
    """
    print('>> Handling latest "WORLD BANK / inflation / country" data')
    raw_inflation_file = source_config.inflation_data_files['raw']['latest']
    inflation_processed_file = source_config.inflation_data_files['processed'][
        'latest']
    inflation_data_raw = pd.read_excel(raw_inflation_file, skiprows=3)
    inflation_data_list = [['country', 'indicator_type', 'year',
                            'indicator_value']]
    for _, row in inflation_data_raw.iterrows():
        country = row['Country Name']
        for year in range(1960, 2030):
            try:
                inflation_value = row[str(year)]
                if ~np.isnan(inflation_value):
                    inflation_data_list.append(
                        [country, 'world_bank_inflation',
                         year, inflation_value])
            except KeyError:
                pass
    inflation_data = pd.DataFrame(inflation_data_list[1:],
                                  columns=inflation_data_list[0])
    write_excel_file(inflation_data, inflation_processed_file)
