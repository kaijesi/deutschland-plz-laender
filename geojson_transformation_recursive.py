#!/usr/bin/python
import pathlib
import json
import os

directory = '/Users/kjesionowski/Desktop/postleitzahlen/rohdaten_bundeslaender'

# standard geojson file

index = 0
for file in os.listdir(directory):
    if '/Users/kjesionowski/Desktop/postleitzahlen/rohdaten_bundeslaender/' + file != '/Users/kjesionowski/Desktop/postleitzahlen/rohdaten_bundeslaender/.DS_Store':
        f = open('/Users/kjesionowski/Desktop/postleitzahlen/rohdaten_bundeslaender/' + file, 'r')
        json_contents = json.loads(f.read())
        features = json_contents["features"]
        for i in features:
            i["id"] = i["properties"]["plz"]
        json_contents["features"] = features
        # Normalized geojson for Tableau map
        out_file_name = file.split('.')
        out_file = open(out_file_name[0] + '_bereinigt.geojson', "w")
        out_file.write(json.dumps(json_contents))
        out_file.close()
        print('Success: ' + out_file_name[0])
        print(index)
        index += 1