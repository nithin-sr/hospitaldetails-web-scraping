import csv
import json

csvfile = open('index1.csv', 'r')
jsonfile = open('jj1.json', 'w')

fieldnames = ("A","B","C","D","E","F","G","H","I","J","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('fieldnames')