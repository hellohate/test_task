import pandas as pd
import requests
import sys
from typing import List


class CSVHandler:
    def __init__(self, url: str):
        self.url = url

    def download(self) -> str:
        """Download the CSV file from Google Drive and save it to a temporary location.

        Returns:
            str: The file path to the downloaded CSV file.
        """
        file_id = self.url.split('/d/')[1].split('/')[0]
        direct_url = f'https://drive.google.com/uc?id={file_id}&export=download'
        response = requests.get(direct_url)
        response.raise_for_status()
        file_path = '/tmp/test_task_data.csv'
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_path

    @staticmethod
    def read(file_path: str, fields: List[str]) -> pd.DataFrame:
        """Read the specified fields from the CSV file.

        Args:
            file_path (str): The file path to the CSV file.
            fields (List[str]): The list of fields to read from the CSV file.

        Returns:
            pd.DataFrame: A DataFrame containing the specified fields.
        """
        try:
            df = pd.read_csv(file_path, usecols=fields)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        return df
