#!python3
# removeCsvHeader.py - removes the headers from all CSV files in the current working directory

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

for csvFile in os.listdir('.'):
    if not csvFile.endswith('.csv'):
        continue
    print(f'Removing header from {csvFile} ...')
    csvRows = []
    csvFileObj = open(csvFile)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(os.path.join('headerRemoved', csvFile), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()