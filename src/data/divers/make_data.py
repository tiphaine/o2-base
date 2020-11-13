import pandas as pd

from divers import source_config
from utils import write_csv_file


def make_divers_idh2_ile_de_france(decoupage_geo=None):
    """
    Collects and formats "IDH2 / Ile-de-France / commune" data for Ile de France
    by commune (source: Institut Paris Region). Reads the information location
    and outputs in the `source_config.py` file.
    """
    if decoupage_geo is None:
        decoupage_geo = 'commune'
    raw_file = source_config.idh2_idf_files[decoupage_geo]['latest']['raw']
    raw_data = pd.read_csv(raw_file)
    output_file = source_config.idh2_idf_files[decoupage_geo][
        'latest']['processed']
    write_csv_file(raw_data, output_file=output_file)
