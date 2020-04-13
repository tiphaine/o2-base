from src.data.divers import source_config
from src.data.utils import download_file_from_url


def get_divers_idh2_ile_de_france(decoupage_geo=None, verbose=False):
    """Gets latest data on 'IDH2 for Ile de France'."""
    if decoupage_geo is None:
        decoupage_geo = 'commune'
    if verbose is True:
        print('Downloading "IDH2 / Ile-de-France / commune"...')
    input_url = source_config.idh2_idf_url[decoupage_geo]['latest']
    if decoupage_geo in ('commune',):
        output_path = source_config.idh2_idf_files[decoupage_geo]['latest']['raw']
        output_data = download_file_from_url(input_url, output_path)
    return output_data
