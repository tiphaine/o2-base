from laposte import source_config
from utils import download_file_from_url


def get_laposte_base_code_postaux(verbose=False):
    """Gets LA POSTE data about code postaux."""
    if verbose is True:
        print('Downloading LA POSTE base des codes postaux...')
    input_url = source_config.laposte_code_postaux_url
    output_path = source_config.laposte_code_postaux_files['raw']
    output_data = download_file_from_url(input_url, output_path)
    return output_data
