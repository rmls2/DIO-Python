import csv
import json
import pprint


def make_json(csv_file_path):
    with open(csv_file_path, encoding='utf-8') as csvf:
        reader = csv.DictReader(csvf)
        data ={}
        for row in reader:
            number = row.pop("Number")
            data[int(number)] = row
        data = json.dumps(data) # transforma um dicionario python em uma string json
        return data


csvFilePath = r'information.csv'
 
print(make_json(csvFilePath))
