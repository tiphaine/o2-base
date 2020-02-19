from src.data.insee import source_config
from src.data.utils import download_insee_excel


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
