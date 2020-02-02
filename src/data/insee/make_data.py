import pandas as pd

from src.data.insee import source_config
from src.data.insee.utils import write_excel_file_sheets


def make_population_commune():
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
