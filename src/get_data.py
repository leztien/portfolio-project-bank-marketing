
"""
Utilities to download, unzip and load the data
"""


from zipfile import ZipFile
from pathlib import Path

import requests
import pandas as pd


def get_data(destination_directory="Downloads"):

    """
    (down)load the data
    """

    url = r"https://archive.ics.uci.edu/static/public/222/" + "bank+marketing.zip"
    path = Path().home() / destination_directory
    zip_file_name = "bank+marketing.zip"
    zip_member_name = 'bank-additional.zip'
    csv_file_path = 'bank-additional/bank-additional-full.csv'

    df = None

    def download_file():
        print("downloading the file...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(path / zip_file_name, mode="wb") as f:
                f.write(response.content)
        response.close()

    def extract_member():
        with ZipFile(path / zip_file_name, mode='r') as f:
            f.extract(path=path, member=zip_member_name)

    def unzip_member():
        with ZipFile(path / zip_member_name, mode='r') as f:
            f.extract(path=path, member=csv_file_path)

    def read_csv():
        nonlocal df
        df = pd.read_csv(path / csv_file_path, delimiter=';')


    conditions = [
        (path / csv_file_path).is_file(),
        (path / zip_member_name).is_file(),
        (path / zip_file_name).is_file(),
        True
        ]

    funcs = [
        download_file,
        extract_member,
        unzip_member,
        read_csv
        ]

    ix = conditions.index(True)

    for func in funcs[-(ix+1):]:
        func()

    return df



if __name__ == '__main__':
    df = get_data()
    print(type(df))


