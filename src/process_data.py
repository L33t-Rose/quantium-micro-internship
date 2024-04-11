import json
import os

csv_files = os.listdir('./data')
output = []
product_target = 'pink morsel'
for csv_file in csv_files:
    with open(f'./data/{csv_file}','r') as f:
        # Read the file contents,split on \n, and truncate the first column
        content = f.read().splitlines()[1::]
        # Iterate through each row, split on ",", and then process the row
        for row in content:
            arr = row.split(',')
            if not arr[0] == product_target:
                continue
            data = {
                "Sales":float(arr[1].replace('$','')) * int(arr[2]),
                "Date":arr[3],
                "Region":arr[4]
            }
            output.append(data)
            
with open('./output.json','w') as f:
    json.dump(output,f)


