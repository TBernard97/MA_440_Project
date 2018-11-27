'''
[!]INFO QUERY TOOL THAT USES THE DATA USA API
[*]LINK FOR QUERY PARAMTERS => https://github.com/DataUSA/datausa-api/wiki/Data-API#params
[*]EXAMPLE IS ATTACHED TO EMAILS I SENT OUT ON HOW TO QUERY
[!]REMEMBER THAT YOU CAN ONLY QUERY ON A DEFINED TABLE. IF YOU WANT DATA FROM TWO TABLES YOU MUST DO TWO SEPERATE QUERIES
'''

#LIBRARIES
import requests, json, csv

#USER INPUT
show = input('[INPUT] Please enter the show parameter => ')
year = input('[INPUT] Please enter year parameter => ')
required = input('[INPUT] Please enter a list required parameters => ')
data_csv_file = input('[INPUT] Please enter name of data csv file => ')
uni_csv = input('[INPUT] Please enter the name of the university info csv file =>   ')

#REQUIRED LIST SPLIT AND JOIN STRING CONVERSION
requireds = required.split()
required_params = ','.join(requireds)



#API QUERY FOR DATA
url = 'https://api.datausa.io/api/?show={}&required={}&year={}'.format(show, required_params, year)
r = requests.get(url)
data = json.loads(r.text)



#FILE OUTPUT
with open('../Data/{}'.format(data_csv_file), mode='a+', ) as test_file: 
    wr = csv.writer(test_file, quoting=csv.QUOTE_ALL, delimiter=',')
    wr.writerow(data['headers'])
    for row in data['data']:
        print('[RESULT] {}'.format(row))
        wr.writerow(row)
  
#SEPERATE POST JOB FOR UNIVERSITY INFO
uids = []

for row in data['data']:
    uids.append(row[1])

for uid in uids:
    url = 'https://api.datausa.io/attrs/university/{}/'.format(uid)
    r = requests.get(url)
    data = json.loads(r.text)
    with open('../Data/{}'.format(uni_csv), mode='a+') as university_file:
        wr = csv.writer(university_file, delimiter=',')
        for row in data['data']:
            print('[RESULT] {}'.format(row))
            wr.writerow(row)
