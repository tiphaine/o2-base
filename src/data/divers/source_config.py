import os

divers_raw = os.path.join('data', 'raw', 'divers')
divers_processed = os.path.join('data', 'processed', 'divers')

foyers_alloc_bas_revenus_prefix = 'http://data.caf.fr/dataset/79250fae-53f6-4d7c-91da-218e79bdcb60/resource/'


idh2_idf_url = {
    'commune': {
        'latest': 'https://opendata.arcgis.com/datasets/379d17bd30d643269df205477ad4bd11_96.csv?outSR=%7B%22latestWkid%22%3A2154%2C%22wkid%22%3A102110%7D',
    },
}

idh2_idf_files = {
    'commune': {
        'latest': {
            'raw': os.path.join(divers_raw, 'idh2_ile-de-france.csv'),
            'processed': os.path.join(divers_processed, 'idh2_ile-de-france.csv'),
        },
    },
}

