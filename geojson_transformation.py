#!/usr/bin/python
import json
import os
os.chdir(os.path.expanduser('~/Desktop/postleitzahlen'))
# standard geojson file
f = open('niedersachsen.geojson', 'r')
json_contents = json.loads(f.read())
features = json_contents["features"]
for i in features:
    i["id"] = i["properties"]["plz"]
json_contents["features"] = features
# Normalized geojson for Tableau map
out_file = open("niedersachsen_bereinigt.geojson", "w")
out_file.write(json.dumps(json_contents))
out_file.close()