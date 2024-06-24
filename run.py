import os
import json
import argparse
from csv_handler import CSVHandler
from references import OUTPUT, URL


def main():
    parser = argparse.ArgumentParser(description='Fetch data from CSV and return specified fields.')
    parser.add_argument('--fields', required=True, help='Comma-separated list of fields to return')
    args = parser.parse_args()

    fields = args.fields.split(',')

    csv_handler = CSVHandler(URL)

    file_path = csv_handler.download()
    df = csv_handler.read(file_path, fields)
    result = {"data": df.to_dict(orient='records')}

    # Print JSON to console
    print(json.dumps(result, indent=4))

    # Ensure the output directory exists
    os.makedirs(OUTPUT, exist_ok=True)

    # Write JSON to output/data.json
    output_file = os.path.join(OUTPUT, 'data.json')
    with open(output_file, 'w') as outfile:
        json.dump(result, outfile, indent=4)


if __name__ == "__main__":
    main()
