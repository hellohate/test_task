
# Windsor.ai Python Interview Task

This project contains a Python program that fetches data from a CSV file hosted on Google Drive, filters specified fields, and returns the data in JSON format. The JSON output is also saved to a file named `data.json` in an `output` directory.


## Requirements

- Python 3.6 or higher
- `pandas`
- `requests`

## Installation

1. Clone the repository or download the zip file and extract it.
2. Navigate to the project directory.
3. Install the required dependencies:

```python
pip install -r requirements.txt
```

## Usage

Run the program with the specified fields as follows:
```python
python run.py --fields date,campaign,clicks
```
This will fetch the CSV data, filter the specified fields, print the JSON result to the console, and save the JSON to '**output/data.json**'.

In case if you need to change google drive url or modify output directory just move to '**references.py**' and modify certain thing.

## Project Structure
```bash
windsor_ai_task/
├── run.py
├── references.py
├── requirements.txt
├── README.md
├── output/
    └── data.json
```
- '**run.py**': The main program file.
- '**requirements.txt**': The dependencies required for the project.
- '**README.md**': This README file.
- '**output/data.json**': Modified data.

## Example

Running the following command:

```bash
python run.py --fields date,campaign,clicks
```
Will produce a JSON output similar to:
```bash
{
    "data": [
        {
            "date": "2021-11-23",
            "campaign": "campaign1",
            "clicks": 10
        },
        {
            "date": "2021-11-24",
            "campaign": "campaign2",
            "clicks": 20
        }
    ]
}
```
The JSON output will be saved to '**output/data.json**'.
