import os

from ecb import source_config
from utils import download_file_from_url, unzip_file, rename_file


def get_forex():
    """Gets latest Forex to Euros data."""
    print(">> Downloading the latest ECB Forex data...")
    url = source_config.forex_data_url['latest']
    output_zip = source_config.forex_data_files['latest']['zip']
    download_file_from_url(url, output_zip)
    unzip_file(output_zip, source_config.ecb_raw)
    rename_file(os.path.join(source_config.ecb_raw, 'eurofxref-hist.csv'),
                source_config.forex_data_files['latest']['raw'])


