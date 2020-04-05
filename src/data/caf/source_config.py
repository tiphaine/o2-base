import os

caf_raw = os.path.join('data', 'raw', 'caf')
caf_processed = os.path.join('data', 'processed', 'caf')

foyers_alloc_bas_revenus_prefix = 'http://data.caf.fr/dataset/79250fae-53f6-4d7c-91da-218e79bdcb60/resource/'


foyers_alloc_bas_revenus_url = {
    'commune': {
        '2009': '{}c51b0621-9b2a-4031-9859-553b06731ec3/download/BasrevenuCom2009.csv'.format(foyers_alloc_bas_revenus_prefix),
        '2010': '{}4a9e6c6d-0f36-4e1c-897a-e7801a0b35d0/download/BasrevenuCom2010.csv'.format(foyers_alloc_bas_revenus_prefix),
        '2011': '{}29796950-288c-4d25-b3d5-d365dd14a712/download/BasrevenuCom2011.csv'.format(foyers_alloc_bas_revenus_prefix),
        '2012': '{}cbb003eb-46da-4ce2-98ad-e617dfef4e2b/download/BasrevenuCom2012.csv'.format(foyers_alloc_bas_revenus_prefix),
        '2013': '{}c45d1b54-17be-4a80-89a0-5ec832e82599/download/BasrevenuCom2013.csv'.format(foyers_alloc_bas_revenus_prefix),
        '2014': '{}a2e0ac46-d4ac-42cc-a28c-bd6b067004b0/download/BasrevenuCom2014.csv'.format(foyers_alloc_bas_revenus_prefix),
        '2015': '{}2f5e861c-0626-4e91-8745-0a5998b4aca7/download/BasrevenuCom2015.csv'.format(foyers_alloc_bas_revenus_prefix),
        '2016': '{}682daddd-82eb-4c9e-b105-4b06327dd5bb/download/BASREVENUCOM.csv'.format(foyers_alloc_bas_revenus_prefix),
        '2017': '{}682daddd-82eb-4c9e-b105-4b06327dd5bb/download/BASREVENUCOM.csv'.format(foyers_alloc_bas_revenus_prefix),
        '2018': '{}682daddd-82eb-4c9e-b105-4b06327dd5bb/download/BASREVENUCOM.csv'.format(foyers_alloc_bas_revenus_prefix),
    },
}

foyers_alloc_bas_revenus_files = {
    'commune': {
        '2009': {
            'raw': os.path.join(caf_raw, 'caf_foyers_bas_revenus-2009.csv'),
            'processed': os.path.join(caf_processed, 'caf_foyers_bas_revenus-2009.csv'),
        },
        '2010': {
            'raw': os.path.join(caf_raw, 'caf_foyers_bas_revenus-2010.csv'),
            'processed': os.path.join(caf_processed, 'caf_foyers_bas_revenus-2010.csv'),
        },
        '2011': {
            'raw': os.path.join(caf_raw, 'caf_foyers_bas_revenus-2011.csv'),
            'processed': os.path.join(caf_processed, 'caf_foyers_bas_revenus-2011.csv'),
        },
        '2012': {
            'raw': os.path.join(caf_raw, 'caf_foyers_bas_revenus-2012.csv'),
            'processed': os.path.join(caf_processed, 'caf_foyers_bas_revenus-2012.csv'),
        },
        '2013': {
            'raw': os.path.join(caf_raw, 'caf_foyers_bas_revenus-2013.csv'),
            'processed': os.path.join(caf_processed, 'caf_foyers_bas_revenus-2013.csv'),
        },
        '2014': {
            'raw': os.path.join(caf_raw, 'caf_foyers_bas_revenus-2014.csv'),
            'processed': os.path.join(caf_processed, 'caf_foyers_bas_revenus-2014.csv'),
        },
        '2015': {
            'raw': os.path.join(caf_raw, 'caf_foyers_bas_revenus-2015.csv'),
            'processed': os.path.join(caf_processed, 'caf_foyers_bas_revenus-2015.csv'),
        },
        '2016': {
            'raw': os.path.join(caf_raw, 'caf_foyers_bas_revenus-2016+.csv'),
            'processed': os.path.join(caf_processed, 'caf_foyers_bas_revenus-2016.csv'),
        },
        '2017': {
            'raw': os.path.join(caf_raw, 'caf_foyers_bas_revenus-2017+.csv'),
            'processed': os.path.join(caf_processed, 'caf_foyers_bas_revenus-2017.csv'),
        },
        '2018': {
            'raw': os.path.join(caf_raw, 'caf_foyers_bas_revenus-2018+.csv'),
            'processed': os.path.join(caf_processed, 'caf_foyers_bas_revenus-2018.csv'),
        },
    },
}

