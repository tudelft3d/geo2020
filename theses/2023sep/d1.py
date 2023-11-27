import csv
import requests
import yaml
import pandas as pd

d = {}

#with open('responses.xlsx', mode='r') as file:
df = pd.read_excel('responses.xlsx', header=0)
for index, row in df.iterrows():
        url = row['Your research in one image']
        myfile = requests.get(url, allow_redirects=True)

        # Check if the request was successful (status code 200)
        if myfile.status_code == 200:
            a = myfile.headers.get('content-disposition', '').lstrip("attachment; filename=")
            d[row['Family name']] = [row['Given names'], row['1st supervisor'], row['2nd supervisor'],row['Summary of the project'], a]
        else:
            print(f"Failed to download image for {row['Family name']} (Status Code: {myfile.status_code})")

print(d)

with open('theses_2023sep.yaml', 'w') as filey:
    yaml.dump(d, filey)

