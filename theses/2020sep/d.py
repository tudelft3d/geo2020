
import csv 
import requests

d = {}
with open('responses.csv', mode ='r') as file: 
    # reading the CSV file 
    c = csv.DictReader(file)
    
    # displaying the contents of the CSV file 
    for l in c: 
        # print(l) 

        url = l['Your research in one image']
        myfile = requests.get(url, allow_redirects=True)
        a = myfile.headers['content-disposition'].lstrip("attachment; filename=")
        d[l['Family name']] = [l['Given names'], l['1st supervisor'], l['2nd supervisor'], l['Summary of the project '], a]


# print (d)

import yaml


with open(r'thesis_2020.yaml', 'w') as filey:
    documents = yaml.dump(d, filey)
