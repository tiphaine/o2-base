import os

ecb_raw = os.path.join('data', 'raw', 'ecb')
ecb_processed = os.path.join('data', 'processed', 'ecb')

forex_data_url = {
    'latest': 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip?bb94f9c24f01f3d2836c92927a40c3e1',
}

forex_data_files = {
    'latest': {
        'zip': os.path.join(ecb_raw, 'ecb_forex_eur_latest.zip'),
        'raw': os.path.join(ecb_raw, 'ecb_forex_eur_latest.csv'),
        'processed': os.path.join(ecb_processed, ),
    }
}
