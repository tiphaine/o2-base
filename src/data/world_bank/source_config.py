import os

insee_raw = os.path.join('data', 'raw')
insee_processed = os.path.join('data', 'processed')


inflation_data_url = {
    'latest': 'http://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL.ZG?downloadformat=excel'
}

inflation_data_files = {
    'raw': {
        'latest': os.path.join(insee_raw, 'world_bank_inflation_latest.xls')
    },
    'processed': {
        'latest': os.path.join(insee_processed, 'world_bank_inflation_par_pays.xlsx'),
    }

}
