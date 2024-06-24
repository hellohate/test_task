import unittest
import os
import json
import pandas as pd
from csv_handler import CSVHandler


class TestCSVHandler(unittest.TestCase):
    """Unit tests for the CSVHandler class."""

    def setUp(self):
        """Set up test environment before each test."""
        self.sample_data = {
            'date': ['2021-11-23', '2021-11-24'],
            'campaign': ['campaign1', 'campaign2'],
            'clicks': [10, 20]
        }
        self.df = pd.DataFrame(self.sample_data)
        self.file_path = '/tmp/test_sample_data.csv'
        self.df.to_csv(self.file_path, index=False)
        self.output_dir = 'output'
        self.output_file = os.path.join(self.output_dir, 'data.json')

    def test_read_csv_valid_fields(self):
        """Test reading CSV with valid fields."""
        csv_handler = CSVHandler('')
        fields = ['date', 'campaign', 'clicks']
        df = csv_handler.read(self.file_path, fields)
        self.assertEqual(df.shape[1], len(fields))
        self.assertListEqual(list(df.columns), fields)

    def test_read_csv_invalid_field(self):
        """Test reading CSV with an invalid field."""
        csv_handler = CSVHandler('')
        fields = ['date', 'invalid_field']
        with self.assertRaises(SystemExit):
            csv_handler.read(self.file_path, fields)

    def test_json_output(self):
        """Test JSON output generation."""
        csv_handler = CSVHandler('')
        fields = ['date', 'campaign', 'clicks']
        df = csv_handler.read(self.file_path, fields)
        result = {"data": df.to_dict(orient='records')}

        os.makedirs(self.output_dir, exist_ok=True)
        with open(self.output_file, 'w') as outfile:
            json.dump(result, outfile, indent=4)

        with open(self.output_file, 'r') as infile:
            output_data = json.load(infile)

        self.assertEqual(result, output_data)

    def tearDown(self):
        """Clean up test environment after each test."""
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        if os.path.exists(self.output_dir):
            os.rmdir(self.output_dir)


if __name__ == '__main__':
    unittest.main()
