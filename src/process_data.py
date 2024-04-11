import os
import csv

csv_files = os.listdir('./data')
product_target = 'pink morsel'
# newline='' needs to be included because the writer was adding extra blank lines between each row
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
with open('output.csv','+w',newline='') as output_file:
    writer = csv.writer(output_file,delimiter=",",)
    writer.writerow(['sales','data','region'])
    for csv_file in csv_files:
        with open(f'./data/{csv_file}','r') as f:
            # Read the file contents,split on \n, and remove the first column
            content = f.read().splitlines()[1::]
            # Iterate through each row, split on ",", and then process the row
            for row in content:
                arr = row.split(',')
                if not arr[0] == product_target:
                    continue
                data = [
                    float(arr[1].replace('$','')) * int(arr[2]),
                    arr[3],
                    arr[4]
                ]
                writer.writerow(data)


