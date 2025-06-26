import csv
import json

def transform():
    # The path to your CSV file
    csv_file_path = './images.csv'
    # The path where you want to save the JSON file
    json_file_path = './images.json'

    # Read the CSV and convert to JSON
    # Read the CSV and convert to JSON, specifying the delimiter and quotechar
    data = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        # Adjust delimiter to semicolon and quotechar to double quotes
        csv_reader = csv.DictReader(csv_file, delimiter=';', quotechar='"')
        for row in csv_reader:
            # Include only "Image GUID" and "Image Source File Name"
            filtered_row = {
                "imageGuuid": row["Image GUID"],
                "ImageSourceFileName": row["Image Source File Name"]
            }
            data.append(filtered_row)

    # Write the JSON output
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    transform()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
