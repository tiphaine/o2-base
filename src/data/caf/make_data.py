import pandas as pd

from src.data.caf import source_config
from src.data.utils import write_csv_file


def _get_year(p):
    """Get year from string having the DD/MM/YEAR format."""
    date_tokens = p['dtref'].split('/')
    if len(date_tokens) == 3:
        date_year = date_tokens[-1]
    else:
        date_year = None
    return date_year


def _format_column_name(raw_column_name, year):
    """Formats a raw column name to remove: spaces, year and character with
    accents.

    Args:
        raw_column_name (str): a column name
        year: the year tu remove

    Returns:
        (str) The formatted column name.
    """
    raw_column_name = ('_'.join(raw_column_name.lower().split()))
    raw_column_name = raw_column_name.replace('_en_{}_'.format(year), '_')
    formatted_column_name = raw_column_name.replace('é', 'e')
    return formatted_column_name


def make_caf_foyers_bas_revenus(decoupage_geo=None):
    """
    Collects and formats 'allocations foyers bas revenus' data for France by
    commune (source INSEE). Reads the information location and outputs in the
    `source_config.py` file.
    """
    if decoupage_geo is None:
        decoupage_geo = 'commune'
    for year, file_paths in source_config.foyers_alloc_bas_revenus_files[
            decoupage_geo].items():
        raw_cols = []
        raw_file = file_paths['raw']
        for item in pd.read_csv(raw_file, sep=';',
                                encoding='ISO-8859-1').columns:
            raw_cols.append(_format_column_name(item, year))
        raw_data = pd.read_csv(raw_file, sep=';',
                               encoding='ISO-8859-1')
        raw_data.columns = raw_cols
        output_file = source_config.foyers_alloc_bas_revenus_files[
            decoupage_geo][year]['processed']
        if int(year) <= 2015:
            raw_data['year'] = year
        else:
            raw_data['year'] = raw_data.apply(_get_year, axis=1)
            raw_data = raw_data[raw_data.year == year]
            raw_data.drop(['dtref'], axis=1, inplace=True)
        write_csv_file(raw_data, output_file=output_file)
