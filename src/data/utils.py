import os
import pandas as pd
import requests
import zipfile


def download_file_from_url(url, output_file, verbose=False):
    """Downloads data from url.

        Args:
            url (str): An url to request for the excel data.
            output_file (str): The output filepath.
            verbose (boolean): A verbose indicator.

        Returns:
            None
        """
    if verbose is True:
        print('Downloading "{}"...'.format(url))
    resp = requests.get(url)
    output = open(output_file, 'wb')
    output.write(resp.content)
    output.close()
    print('File available -> "{}".'.format(output_file))
    return output_file


def unzip_file(zip_path, output_dir, verbose=False):
    """Unzips all the contents of a zip file to a given directory.

        Args:
            zip_path (str): The Zip file path.
            output_dir (str): The output directory.
            verbose (bool): A boolean for verbosity.

        Returns:
            None
    """
    if verbose is True:
        print('Extracting "{}" to "{}"...'.format(zip_path, output_dir))
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    print('Zip files extracted to -> "{}".'.format(output_dir))
    return output_dir


def rename_file(file_source, file_dest):
    """Renames a file from file_source to file_dest.

    Args:
        file_source (str): The file to rename path.
        file_dest (str): The new file name.

    Returns:
        None
    """
    os.rename(file_source, file_dest)
    print('File renamed from "{}" to "{}".'.format(file_source, file_dest))


def download_insee_excel(url, output_file, verbose=False, check=True):
    """Downloads data from url to an Excel file.

        Args:
            url (str): An url to request for the excel data.
            output_file (str): The output excel filepath.
            verbose (boolean): A verbose indicator.
            check (boolean): If True, this checks that the url ends with 'xls'
                or 'xlsx' which is not mandatory.

        Returns:
            None

        Raises:
            May raise a ValueError if the url ending does not end with 'xls' or
        'xlsx'.
        """
    if check is True:
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


def write_csv_file(dataframe, output_file):
    """Writes data from dataframe in the Excel file.

    Args:
        dataframe (pandas dataframe): A dataframe.
        output_file (str): The output excel filepath.

    Returns:
        None

    Raises:
        ValueError if the output file is not an Excel file.
    """
    if output_file.split('.')[-1] not in ('csv', ):
        raise ValueError('Wrong output file type.')
    dataframe.to_csv(output_file, index=False)
    print('Data written in "{}'.format(output_file))
