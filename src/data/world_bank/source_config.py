import os

world_bank_raw = os.path.join('data', 'raw', 'world-bank')
world_bank_processed = os.path.join('data', 'processed', 'world-bank')

inflation_data_url = {
    'latest': 'http://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL.ZG?downloadformat=excel'
}

inflation_data_files = {
    'raw': {
        'latest': os.path.join(world_bank_raw, 'world_bank_inflation_latest.xls')
    },
    'processed': {
        'latest': os.path.join(world_bank_processed, 'world_bank_inflation_par_pays.xlsx'),
    }

}
