from world_bank import source_config
from utils import download_insee_excel


def get_inflation_country():
    """Downloads latest World Bank data about inflation (Inflation, consumer
    prices (annual %).
    Source: https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG
    """
    print(">> Downloading WORLD BANK inflation / country data...")
    url = source_config.inflation_data_url['latest']
    output_file = source_config.inflation_data_files['raw']['latest']
    download_insee_excel(url, output_file, check=False)
