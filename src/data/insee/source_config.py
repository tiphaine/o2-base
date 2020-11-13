import os

insee_raw = os.path.join('data', 'raw', 'insee')
insee_processed = os.path.join('data', 'processed', 'insee')

population_data_url = {
    'commune': {
        '2017': 'https://www.insee.fr/fr/statistiques/fichier/3698339/base-pop-historiques-1876-2017.xls',
    },
}

confiance_data_url = {
    'menage': {
        '2020': {
            1: 'https://www.insee.fr/fr/statistiques/fichier/4295756/les_series_longues.xls',
            2: 'https://www.insee.fr/fr/statistiques/fichier/4317593/Camme_202002.xls',
            10: 'https://www.insee.fr/fr/statistiques/fichier/4922879/Camme_202010.xls',
        }
    }
}

affaires_url = {
    'batiment': {
        '2020': {
            1: 'https://www.insee.fr/fr/statistiques/fichier/4292621/conj_bat_202001_FR.xls',
            2: 'https://www.insee.fr/fr/statistiques/fichier/4317274/conj_bat_202002.xls',
            10: 'https://www.insee.fr/fr/statistiques/fichier/4808692/IRbati1020.xls',
        }

    }
}

couple_famille_menages_url = {
    'commune': {
        '2011': 'https://www.insee.fr/fr/statistiques/fichier/2044612/base-cc-coupl-fam-men-2011.xls',
        '2012': 'https://www.insee.fr/fr/statistiques/fichier/2044618/base-cc-coupl-fam-men-2012.xls',
        '2013': 'https://www.insee.fr/fr/statistiques/fichier/2044615/base-cc-coupl-fam-men-2013.xls',
        '2014': 'https://www.insee.fr/fr/statistiques/fichier/2862009/base-cc-coupl-fam-men-2014.zip',
        '2015': 'https://www.insee.fr/fr/statistiques/fichier/3565598/base-cc-coupl-fam-men-2015.zip',
        '2016': 'https://www.insee.fr/fr/statistiques/fichier/4171359/base-cc-coupl-fam-men-2016-xls.zip',
    },
}

diplome_formations_url = {
    'commune': {
        '2010': 'https://www.insee.fr/fr/statistiques/fichier/2044702/base-cc-diplomes-formation-2010.zip',
        '2011': 'https://www.insee.fr/fr/statistiques/fichier/2044704/base-cc-diplomes-formation_2011.xls',
        '2012': 'https://www.insee.fr/fr/statistiques/fichier/2044707/base-cc-diplomes-formation_2012.zip',
        '2013': 'https://www.insee.fr/fr/statistiques/fichier/2044692/base-cc-diplomes-formation-2013_v2.xls',
        '2014': 'https://www.insee.fr/fr/statistiques/fichier/2862015/base-cc-dipl-formation-2014.zip',
        '2015': 'https://www.insee.fr/fr/statistiques/fichier/3564182/base-cc-dipl-formation-2015.zip',
        '2016': 'https://www.insee.fr/fr/statistiques/fichier/4171395/base-cc-dipl-formation-2016-xls.zip',
    },
}

affaires_files = {
    'batiment': {
        '2020': {
            'raw': os.path.join(insee_raw, 'insee_affaires_batiment.xls'),
            'processed': os.path.join(insee_processed, ),
        }
    }
}

couple_famille_menages_files = {
    'commune': {
        '2011': {
            'raw': os.path.join(insee_raw, 'base-ic-couples-familles-menages-communes-2011.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2012': {
            'raw': os.path.join(insee_raw, 'base-ic-couples-familles-menages-communes-2012.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2013': {
            'raw': os.path.join(insee_raw, 'base-ic-couples-familles-menages-communes-2013.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2014': {
            'zip': os.path.join(insee_raw, 'base-ic-couples-familles-menages-communes-2014.zip'),
            'raw': os.path.join(insee_raw, 'base-cc-coupl-fam-men-2014.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2015': {
            'zip': os.path.join(insee_raw, 'base-ic-couples-familles-menages-communes-2015.zip'),
            'raw': os.path.join(insee_raw, 'base-cc-coupl-fam-men-2015.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2016': {
            'zip': os.path.join(insee_raw, 'base-ic-couples-familles-menages-communes-2016.zip'),
            'raw': os.path.join(insee_raw, 'base-cc-coupl-fam-men-2016.xls'),
            'processed': os.path.join(insee_processed, ),
        },
    },
}

diplome_formation_files = {
    'commune': {
        '2010': {
            'zip': os.path.join(insee_raw, 'base-cc-diplomes-formation-communes-2010.zip'),
            'raw': os.path.join(insee_raw, 'base-cc-diplomes-formation-2010.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2011': {
            'raw': os.path.join(insee_raw, 'base-cc-diplomes-formation-2011.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2012': {
            'zip': os.path.join(insee_raw, 'base-cc-diplomes-formation-communes-2012.zip'),
            'raw': os.path.join(insee_raw, 'base-cc-diplomes-formation_2012.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2013': {
            'raw': os.path.join(insee_raw, 'base-cc-diplomes-formation-2013.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2014': {
            'zip': os.path.join(insee_raw, 'base-cc-diplomes-formation-communes-2014.zip'),
            'raw': os.path.join(insee_raw, 'base-cc-diplomes-formation-2014.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2015': {
            'zip': os.path.join(insee_raw, 'base-cc-diplomes-formation-communes-2015.zip'),
            'raw': os.path.join(insee_raw, 'base-cc-diplomes-formation-2015.xls'),
            'processed': os.path.join(insee_processed, ),
        },
        '2016': {
            'zip': os.path.join(insee_raw, 'base-cc-diplomes-formation-communes-2016.zip'),
            'raw': os.path.join(insee_raw, 'base-cc-diplomes-formation-2016.xls'),
            'processed': os.path.join(insee_processed, ),
        },
    },
}

population_data_raw_file = {
    'commune': {
        '2017': os.path.join(insee_raw, 'insee_population_2017.xls')
    }
}

confiance_data_raw_file = {
    'menage': {
        '2020': {
            1: os.path.join(insee_raw, 'insee_confiance_menages_2020-01.xls'),
            2: os.path.join(insee_raw, 'insee_confiance_menages_2020-02.xls'),
            10: os.path.join(insee_raw, 'insee_confiance_menages_2020-10.xls'),
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
            1: os.path.join(insee_processed, ),
            2: os.path.join(insee_processed, ),
            10: os.path.join(insee_processed, ),
        }
    }
}
