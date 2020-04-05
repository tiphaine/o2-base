from src.data.caf import source_config
from src.data.utils import download_file_from_url


def get_caf_alloc_foyers_bas_revenus(decoupage_geo=None, verbose=False):
    """Gets all CAF data about 'allocations foyers bas revenus'."""
    if decoupage_geo is None:
        decoupage_geo = 'commune'
    output_datas = {}
    for year in source_config.foyers_alloc_bas_revenus_url[decoupage_geo].keys():
        if verbose is True:
            print('Downloading CAF foyers allocations bas '
                  'revenus / commune / {}...'.format(year))
        input_url = source_config.foyers_alloc_bas_revenus_url[
            decoupage_geo][year]
        if decoupage_geo in ('commune',):
            if input_url.endswith('csv'):
                output_path = source_config.foyers_alloc_bas_revenus_files[
                    decoupage_geo][year]['raw']
                output_data = download_file_from_url(input_url, output_path)
                output_datas[year] = output_data
    return output_datas
