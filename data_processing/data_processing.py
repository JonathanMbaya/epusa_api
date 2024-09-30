import os
import json

files_location = "../names"

def data_to_json(line: str, year: int):
    lineArray = line.strip().split(",")
    lineObject = {
        "year": year,
        "firstname": lineArray[0],
        "gender": lineArray[1],
        "nb_occur": int(lineArray[2])
    }
    return lineObject

def files_to_list(files_location: str, max_records_per_file=100):
    dataList = []
    for file_name in os.listdir(files_location):
        if file_name.endswith(".txt"):     
            file_path = os.path.join(files_location, file_name)
            print(f"Processing file: {file_path}")
            
            with open(file_path, "r") as txt_file:
                year = int(file_name[3:7])
                record_count = 0
                
                for line in txt_file:
                    if record_count < max_records_per_file:
                        dataList.append(data_to_json(line, year))
                        record_count += 1
                    else:
                        break  # Stop reading after 100 records
    return dataList

# Charger les données des fichiers et limiter à 100 prénoms par fichier
data = files_to_list(files_location, max_records_per_file=100)

# Sauvegarder les données dans un fichier JSON
output_path = "./output_data/name.json"
with open(output_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Data saved to {output_path}")