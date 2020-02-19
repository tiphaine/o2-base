import os

insee_raw = os.path.join('data', 'raw', 'insee')
insee_processed = os.path.join('data', 'processed', 'insee')

world_bank_raw = os.path.join('data', 'raw', 'world-bank')
world_bank_processed = os.path.join('data', 'processed', 'world-bank')


population_data_url = {
    'commune': {
        '2017': 'https://www.insee.fr/fr/statistiques/fichier/3698339/base-pop-historiques-1876-2017.xls',
    },
}

confiance_data_url = {
    'menage': {
        '2020': {
            1: 'https://www.insee.fr/fr/statistiques/fichier/4295756/les_series_longues.xls'
        }
    }
}

affaires_url = {
    'batiment': {
        '2020': {
            1: 'https://www.insee.fr/fr/statistiques/fichier/4292621/conj_bat_202001_FR.xls'
        }

    }
}

affaires_files = {
    'batiment': {
        '2020': {
            'raw': os.path.join(insee_raw, 'insee_affaires_batiment.xls'),
            'processed': os.path.join(insee_processed, ),
        }
    }
}

population_data_raw_file = {
    'commune': {
        '2017': os.path.join(insee_raw, 'insee_population_2017.xls')
    }
}

confiance_data_raw_file = {
    'menage': {
        '2020': {
            1: os.path.join(insee_raw, 'insee_confiance_menages_2020-01.xls')
        }
    }
}

population_processed_file = {
    'commune': {
        '2017': {
            'annee': os.path.join(insee_processed, 'insee_population_commune_2017_par_annee.xlsx'),
            'region': os.path.join(insee_processed, 'insee_population_commune_2017_par_dept.xlsx'),
        }
    }
}

confiance_data_processed_file = {
    'menage': {
        '2020': {
            1: os.path.join(insee_processed, )
        }
    }
}
