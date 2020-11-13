import pandas as pd
import os

from insee import source_config
from utils import write_excel_file_sheets, write_excel_file
from helpers import month_abr_fr_to_number

from collections import defaultdict


def _insee_format_column_name(col, year):
    """Formats a raw column name to remove: spaces, year and character with
    accents.

    Args:
        col (str): a column name
        year: the year tu remove

    Returns:
        (str) The formatted column name.

    """
    raw_column_name = ('_'.join(col.lower().split()))
    raw_column_name = raw_column_name.replace('_en_{}_'.format(year), '_')
    formatted_column_name = raw_column_name.replace('é', 'e')
    return formatted_column_name


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
    res = defaultdict(list)
    for col_name in raw_cols[1:]:
        for index, row in confiance_raw.iterrows():
            date_year = pd.to_datetime(row['date']).year
            date_month = pd.to_datetime(row['date']).month
            res[col_name].append([date_year, date_month, col_name, row[col_name]])
        output_data = pd.DataFrame(res[col_name], columns=['year', 'month', 'indicator_type', 'indicator_value'])
        output_file = os.path.join(confiance_processed_file_prefix, 'insee_confiance_{}.xls'.format(col_name))
        write_excel_file(output_data, output_file=output_file)


def make_climat_affaires_batiment():
    """
    Collects and formats climat des affaires / batiment for France (source:
    INSEE). Reads the information location and outputs in the `source_config.py`
    file.
    """
    print('>> Handling "INSEE Climat des Affaires / Batiment" data for year...')
    raw_cols = [
        'date',
        'retournement',
        'affaires_batiment_synthetique',
        'activite_passe',
        'activite_passe_clientele_publique',
        'activite_passe_clientele_privee',
        'activite_passe_logement_neuf',
        'activite_passe_neuf_hors_logement',
        'activite_passe_entretien_amelioration',
        'activite_prevue',
        'activite_prevue_clientele_publique',
        'activite_prevue_clientele_privee',
        'activite_prevue_logement_neuf',
        'activite_prevue_hors_logement_neuf',
        'activite_prevue_entretien_amelioration',
        'jugement_carnet_commande',
        'carnet_commande_par_mois',
        'perspective_generale_activite',
        'tx_utilisation_capa_production',
        'entreprise_sans_accroiss_production',
        'entreprise_sans_accroiss_production_insuf_mat',
        'entreprise_sans_accroiss_production_insuf_pers',
        'entreprise_sans_accroiss_production_insuf_approv',
        'entreprise_sans_accroiss_production_cond_climat',
        'entreprise_difficulte_recrutement',
        'tendance_effectif_passe',
        'tendance_effectif_prevu',
        'evolution_prevue_prix',
        'situation_tresorerie',
        'delais_paiement',
        'delais_paiement_client_public',
        'delais_paiement_client_prive',
    ]
    latest_year = str(max(
        [int(item) for item in source_config.affaires_files[
            'batiment'].keys()]))
    raw_aff_bat_file = source_config.affaires_files['batiment'][latest_year][
        'raw']
    print(raw_aff_bat_file)
    aff_bat_raw = pd.read_excel(raw_aff_bat_file,
                                sheet_name='Ensemble', skiprows=6)
    print(aff_bat_raw.shape)
    aff_bat_raw.columns = raw_cols
    aff_bat_processed_file_prefix = source_config.affaires_files['batiment'][
        latest_year]['processed']
    res = defaultdict(list)
    for col_name in raw_cols[1:]:
        for index, row in aff_bat_raw.iterrows():
            month_raw, date_year = row['date'].split()
            date_month = month_abr_fr_to_number[month_raw.replace('.', '')]
            res[col_name].append([date_year, date_month, col_name,
                                 row[col_name]])
        output_data = pd.DataFrame(res[col_name], columns=[
            'year', 'month', 'indicator_type', 'indicator_value'])
        output_file = os.path.join(
            aff_bat_processed_file_prefix,
            'insee_affaires_batiment_{}.xls'.format(col_name))
        write_excel_file(output_data, output_file=output_file)


def make_insee_couple_famille_menages(decoupage_geo=None):
    """
    Collects and formats 'couple famille menages' data for France (source:
    INSEE). Reads the information location and outputs in the `source_config.py`
    file.
    """
    if decoupage_geo is None:
        decoupage_geo = 'commune'
    for year, file_paths in source_config.couple_famille_menages_files[
            decoupage_geo].items():
        raw_cols = []
        raw_file = file_paths['raw']
        for item in pd.read_excel(raw_file, skiprows=4).columns:
            raw_cols.append(_insee_format_column_name(item, year))
        raw_data = pd.read_excel(raw_file, skiprows=5)
        raw_data.columns = raw_cols
        raw_data['year'] = year
        for col_prefix in ('men', 'pop', 'fam'):
            col_list = [col for col in raw_cols if col.startswith(col_prefix)]
            res = defaultdict(list)
            for col_name in col_list:
                for index, row in raw_data.iterrows():
                    res[col_name].append([
                        row['year'],
                        row['code_geographique'],
                        row['region'],
                        row['departement'],
                        row['libelle_geographique'],
                        col_name, row[col_name]])
                output_data = pd.DataFrame(res[col_name], columns=[
                    'year', 'code_geographique', 'region', 'departement',
                    'libelle_geographique', 'indicator_type',
                    'indicator_value'])
                couple_famille_menages_processed_file_prefix = \
                    source_config.couple_famille_menages_files[
                        decoupage_geo][year]['processed']
                output_file = os.path.join(
                    couple_famille_menages_processed_file_prefix,
                    'insee_couple_famille_menages_commune_{}_{}.xls'.format(
                        col_name, year))
                write_excel_file(output_data, output_file=output_file)


def make_insee_diplome_formation(decoupage_geo=None):
    """
    Collects and formats 'diplome formation' data for France (source:
    INSEE). Reads the information location and outputs in the `source_config.py`
    file.
    """
    if decoupage_geo is None:
        decoupage_geo = 'commune'
    output_files = {}
    print('>> Handling "INSEE diplome formation" data for year...')
    for year, file_paths in source_config.diplome_formation_files[
            decoupage_geo].items():
        print('\t- {}'.format(year))
        output_files[year] = {}
        raw_cols = []
        raw_file = file_paths['raw']
        for item in pd.read_excel(raw_file, skiprows=4).columns:
            raw_cols.append(_insee_format_column_name(item, year))
        raw_data = pd.read_excel(raw_file, skiprows=5)
        raw_data.columns = raw_cols
        raw_data['year'] = year
        for col_prefix in ('pop', 'hommes', 'femmes'):
            col_list = [col for col in raw_cols if col.startswith(col_prefix)]
            res = defaultdict(list)
            res[col_prefix].append(
                ['year', 'code_geographique', 'region', 'departement',
                 'libelle_geographique'] + col_list)
            for index, row in raw_data.iterrows():
                line_base = [
                        row['year'],
                        row['code_geographique'],
                        row['region'],
                        row['departement'],
                        row['libelle_geographique'],]
                for col_name in col_list:
                    line_base.append(row[col_name])
                res[col_prefix].append(line_base)
            output_data = pd.DataFrame(res[col_prefix][1:],
                                       columns=res[col_prefix][0])
            diplome_formation_files_prefix = source_config.diplome_formation_files[
                decoupage_geo][year]['processed']
            output_file = os.path.join(
                diplome_formation_files_prefix,
                'insee_diplome_formation_{}_commune_{}.xls'.format(
                    col_prefix, year))
            write_excel_file(output_data, output_file=output_file)
            output_files[year][col_prefix] = output_file
    return output_files
