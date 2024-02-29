import os
import json
import csv
import pickle

def get_directory_info(directory):
    directory_info = []
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            dir_path = os.path.join(root, d)
            dir_size = sum(os.path.getsize(os.path.join(dir_path, f)) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)))
            directory_info.append({
                'name': d,
                'parent': root,
                'type': 'directory',
                'size': dir_size
            })
        for f in files:
            file_path = os.path.join(root, f)
            file_size = os.path.getsize(file_path)
            directory_info.append({
                'name': f,
                'parent': root,
                'type': 'file',
                'size': file_size
            })
    return directory_info

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = ['name', 'parent', 'type', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def save_to_pickle(data, filename):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

def save_directory_info(directory, json_filename, csv_filename, pickle_filename):
    directory_info = get_directory_info(directory)
    save_to_json(directory_info, json_filename)
    save_to_csv(directory_info, csv_filename)
    save_to_pickle(directory_info, pickle_filename)

