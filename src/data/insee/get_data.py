from insee import source_config
from utils import download_insee_excel, download_file_from_url, unzip_file


def get_population_commune(verbose=False):
    """Downloads latest INSEE data about population."""
    print(">> Downloading INSEE population / commune data...")
    latest_year = str(max(
        [int(item) for item in source_config.population_data_url[
            'commune'].keys()]))
    if verbose is True:
        print('INSEE POPULATION / Latest available data is from {}.'.format(
            latest_year))
    url = source_config.population_data_url['commune'][latest_year]
    output_file = source_config.population_data_raw_file['commune'][latest_year]
    download_insee_excel(url, output_file)


def get_confiance_menages(verbose=False):
    """Gets latest INSEE data about 'confiance des menages'."""
    print(">> Downloading INSEE confiance des menages data...")
    latest_year = str(max(
        [int(item) for item in source_config.confiance_data_url[
            'menage'].keys()]))
    latest_month = max([int(item) for item in source_config.confiance_data_url[
            'menage'][latest_year].keys()])
    if verbose is True:
        print('INSEE CONFIANCE MENAGE / Latest available data is from {}-{}.'.format(
            latest_year, latest_month))
    url = source_config.confiance_data_url['menage'][latest_year][latest_month]
    output_file = source_config.confiance_data_raw_file['menage'][latest_year][latest_month]
    download_insee_excel(url, output_file)


def get_affaires_batiment(verbose=False):
    """Gets latest INSEE data about 'climat des affaires / batiment'."""
    print(">> Downloading INSEE climat des affaires / batiment data...")
    latest_year = str(max(
        [int(item) for item in source_config.affaires_url[
            'batiment'].keys()]))
    latest_month = max([int(item) for item in source_config.affaires_url[
            'batiment'][latest_year].keys()])
    if verbose is True:
        print('INSEE AFFAIRES BATIMENT / Latest available data is from'
              ' {}-{}.'.format(latest_year, latest_month))
    url = source_config.affaires_url['batiment'][latest_year][latest_month]
    output_file = source_config.affaires_files['batiment'][
        latest_year]['raw']
    download_insee_excel(url, output_file)


def get_insee_couple_famille_menages(decoupage_geo=None, verbose=False):
    """Gets all INSEE data about 'couple famille menages'."""
    if decoupage_geo is None:
        decoupage_geo = 'commune'
    output_datas = []
    for year in source_config.couple_famille_menages_url[decoupage_geo].keys():
        if verbose is True:
            print('Downloading INSEE couple-famille-menage / commune / '
                  '{}...'.format(year))
        input_url = source_config.couple_famille_menages_url[
            decoupage_geo][year]
        if decoupage_geo in ('commune',):
            if input_url.endswith('xls') or input_url.endswith('xlsx'):
                output_file = source_config.couple_famille_menages_files[
                    decoupage_geo][year]['raw']
                output_data = download_insee_excel(input_url, output_file)
            elif input_url.endswith('zip'):
                output_file = source_config.couple_famille_menages_files[
                    decoupage_geo][year]['zip']
                output_zip = download_file_from_url(input_url, output_file)
                unzip_file(output_zip, source_config.insee_raw)
                output_data = source_config.couple_famille_menages_files[
                    decoupage_geo][year]['raw']
        output_datas.append(output_data)
    return output_datas


def get_insee_diplome_formation(decoupage_geo=None, verbose=False):
    """Gets all INSEE data about 'diplome formation'."""
    if decoupage_geo is None:
        decoupage_geo = 'commune'
    output_datas = []
    for year in source_config.diplome_formations_url[decoupage_geo].keys():
        if verbose is True:
            print('Downloading INSEE diplome-formation / commune / {}...'.format(year))
        input_url = source_config.diplome_formations_url[decoupage_geo][year]
        if decoupage_geo in ('commune',):
            if input_url.endswith('xls') or input_url.endswith('xlsx'):
                output_path = source_config.diplome_formation_files[decoupage_geo][year]['raw']
                output_data = download_insee_excel(input_url, output_path)
            elif input_url.endswith('zip'):
                output_path = source_config.diplome_formation_files[decoupage_geo][year]['zip']
                output_zip = download_file_from_url(input_url, output_path)
                unzip_file(output_zip, source_config.insee_raw)
                output_data = source_config.diplome_formation_files[decoupage_geo][year]['raw']
        output_datas.append(output_data)
