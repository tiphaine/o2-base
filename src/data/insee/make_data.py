import pandas as pd
import os

from src.data.insee import source_config
from src.data.insee.utils import write_excel_file_sheets, write_excel_file


def make_population_commune():
    """
    Collects and formats population data for France by commune (source
    INSEE). Reads the information location and outputs in the
    `source_config.py` file.
    """
    print('>> Handling "INSEE / population / commune" data for year :')
    latest_year = str(max(
        [int(item) for item in source_config.population_data_raw_file[
            'commune'].keys()]))
    raw_pop_file = source_config.population_data_raw_file['commune'][latest_year]
    pop_processed_annee_file = source_config.population_processed_file[
        'commune'][latest_year]['annee']
    pop_processed_dept_file = source_config.population_processed_file[
        'commune'][latest_year]['region']
    pop_data = pd.read_excel(raw_pop_file, skiprows=5)
    pop_output = [
        ['code_geo', 'region', 'departement', 'libelle_geo',
         'type_geo', 'annee', 'population']]
    stub_cols = ['CODGEO', 'REG', 'DEP', 'LIBGEO']
    for col in [col for col in pop_data.columns if col not in stub_cols]:
        if col.startswith('PMUN'):
            year = 2000 + int(col[-2:])
        elif col.startswith('PSDC'):
            year = 1900 + int(col[-2:])
        elif col.startswith('PTOT'):
            if len(col) == 6:
                year = 1900 + int(col[-2:])
            else:
                year = int(col[-4:])
        print('\t- {}'.format(year))
        selected_df = pop_data[stub_cols + [col]]
        for index, row in selected_df.iterrows():
            pop_output.append(
                [row['CODGEO'], row['REG'], row['DEP'], row['LIBGEO'],
                 'commune', year, row[col]])
    pop_formatted_data = pd.DataFrame(pop_output[1:], columns=pop_output[0])
    pop_formatted_data['annee'] = pop_formatted_data.annee.astype(str)
    print('>> Writing yearly data...')
    yearly_dfs = {}
    for annee in pop_formatted_data['annee'].unique():
        yearly_dfs[annee] = pop_formatted_data[
            pop_formatted_data.annee == annee]
    write_excel_file_sheets(yearly_dfs, output_file=pop_processed_annee_file)
    print('>> Writing data by departement...')
    communes_dfs = {}
    for departement in pop_formatted_data['departement'].unique():
        communes_dfs[departement] = pop_formatted_data[
            pop_formatted_data.departement == departement]
    write_excel_file_sheets(communes_dfs, output_file=pop_processed_dept_file)


def make_confiance_menages():
    """
    Collects and formats confiance des menages data for France  (source INSEE).
    Reads the information location and outputs in the `source_config.py` file.
    """
    print('>> Handling "INSEE Confiance Menages" data for year...')
    raw_cols = [
        'date',
        'confiance_menage_synthetique',
        'niveau_vie_passe',
        'niveau_vie_perspective',
        'chomage_perspective',
        'prix_passe',
        'prix_perspective',
        'opportunite_achat_important',
        'opportunite_epargne',
        'epargne_capa_actuelle',
        'finance_pers_passe',
        'finance_pers_perspective',
        'epargne_capa_perspective'
    ]
    latest_year = str(max(
        [int(item) for item in source_config.confiance_data_url[
            'menage'].keys()]))
    latest_month = max([int(item) for item in source_config.confiance_data_url[
        'menage'][latest_year].keys()])
    raw_confiance_file = source_config.confiance_data_raw_file['menage'][latest_year][latest_month]
    confiance_raw = pd.read_excel(raw_confiance_file, skiprows=5)
    confiance_raw.columns = raw_cols
    confiance_processed_file_prefix = source_config.confiance_data_processed_file[
        'menage'][latest_year][latest_month]
    from collections import defaultdict
    res = defaultdict(list)
    for col_name in raw_cols[1:]:
        for index, row in confiance_raw.iterrows():
            date_year = pd.to_datetime(row['date']).year
            date_month = pd.to_datetime(row['date']).month
            res[col_name].append([date_year, date_month, col_name, row[col_name]])
        output_data = pd.DataFrame(res[col_name], columns=['year', 'month', 'indicator_type', 'indicator_value'])
        output_file = os.path.join(confiance_processed_file_prefix, 'insee_confiance_{}.xls'.format(col_name))
        write_excel_file(output_data, output_file=output_file)
