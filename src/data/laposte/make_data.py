import pandas as pd

from laposte import source_config
from utils import write_csv_file


def _format_column_name(raw_column_name, year=None):
    """Formats a raw column name to remove: spaces, year and character with
    accents.

    Args:
        raw_column_name (str): a column name
        year: the year tu remove

    Returns:
        (str) The formatted column name.
    """
    raw_column_name = ('_'.join(raw_column_name.lower().split()))
    if year is not None:
        raw_column_name = raw_column_name.replace('_en_{}_'.format(year), '_')
    formatted_column_name = raw_column_name.replace('é', 'e')
    return formatted_column_name


def make_laposte_base_code_postaux():
    """
    Collects and formats 'base des codes postaux' data for France by
    commune (source LA POSTE). Reads the information location and outputs in
    the `source_config.py` file.
    """
    raw_file = source_config.laposte_code_postaux_files['raw']
    raw_cols = []
    for item in pd.read_csv(raw_file, sep=';', encoding='ISO-8859-1').columns:
        raw_cols.append(_format_column_name(item))
    raw_data = pd.read_csv(raw_file, sep=';', encoding='ISO-8859-1')
    raw_data.columns = raw_cols
    output_file = source_config.laposte_code_postaux_files['processed']
    write_csv_file(raw_data, output_file=output_file)
