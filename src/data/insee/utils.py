import requests
import pandas as pd


def download_insee_excel(url, output_file, verbose=False):
    output_type = url.split('.')[-1]
    if output_type.lower() not in ('xls', 'xlsx',):
        raise ValueError("Wrong file type")
    if verbose is True:
        print('Downloading "{}"...'.format(url))
    resp = requests.get(url)
    output = open(output_file, 'wb')
    output.write(resp.content)
    output.close()
    print('File available -> "{}".'.format(output_file))
    return output_file


def write_excel_file(dataframe, output_file):
    """Writes data from dataframe in the Excel file.

    Args:
        dataframe (pandas dataframe): A dataframe.
        output_file (str): The output excel filepath.

    Returns:
        None

    Raises:
        ValueError if the output file is not an Excel file.
    """
    if output_file.split('.')[-1] not in ('xls', 'xlsx'):
        raise ValueError('Wrong output file type.')
    dataframe.to_excel(output_file, index=False)
    print('Data written in "{}'.format(output_file))


def write_excel_file_sheets(dataframes, output_file):
    """Writes data from dataframes dictionary into multiples sheets in the Excel
    file.

    Args:
        dataframes (dict): A dictionary with sheet names as key and dataframes
            as values. Each item will be written into the corresponding sheet.
        output_file (str): The output excel filepath.

    Returns:
        None

    Raises:
        ValueError if the output file is not an Excel file.
    """
    if output_file.split('.')[-1] not in ('xls', 'xlsx'):
        raise ValueError('Wrong output file type.')
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    for sheet_name, sheet_data in dataframes.items():
        sheet_data.to_excel(
            writer, sheet_name, index=False)
    writer.save()
    writer.close()
    print('Data written in "{}"'.format(output_file))
