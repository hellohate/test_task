import argparse
import pandas as pd
import json
import requests
import sys
import os
from references import OUTPUT, URL


def download_csv(url):
    file_id = url.split('/d/')[1].split('/')[0]
    direct_url = f'https://drive.google.com/uc?id={file_id}&export=download'
    response = requests.get(direct_url)
    response.raise_for_status()
    with open('/tmp/test_task_data.csv', 'wb') as file:
        file.write(response.content)
    return '/tmp/test_task_data.csv'


def read_csv(file_path, fields):
    try:
        df = pd.read_csv(file_path, usecols=fields)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    return df


def main():
    parser = argparse.ArgumentParser(description='Fetch data from CSV and return specified fields.')
    parser.add_argument('--fields', required=True, help='Comma-separated list of fields to return')
    args = parser.parse_args()

    fields = args.fields.split(',')

    file_path = download_csv(URL)

    df = read_csv(file_path, fields)
    result = {"data": df.to_dict(orient='records')}

    print(json.dumps(result, indent=4))

    output_dir = OUTPUT
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, 'data.json')
    with open(output_file, 'w') as outfile:
        json.dump(result, outfile, indent=4)


if __name__ == "__main__":
    main()
