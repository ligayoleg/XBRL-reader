#import libraries
import requests
from bs4 import BeautifulSoup

# define base url
base_url = r"https://www.sec.gov/Archives/edgar/data"

# define cik
cik_num = '/21344/'

# create filling link
fillings_url = base_url + cik_num + '/index.json'

# request the url
content = requests.get(fillings_url)
decoded_content = content.json()

# go and grab a single filing number
filing_number = decoded_content['directory']['item'][0]['name']

# define filing number url
filling_url = base_url + cik_num + filing_number + '/index.json'

# request the url
content = requests.get(filling_url)
doc_content = content.json()

for doc in doc_content['directory']['item']:
    if doc['type'] != 'image2.gif':

        doc_name = doc['name']
        doc_url = base_url + cik_num + filing_number + '/' + doc_name
        print(doc_url)


# grab multiple filings
for filiing in decoded_content['directory']['item']:
    # define each filing number
    fil_num = filiing['name']

    fil_url = base_url + cik_num + fil_num + '/index.json'

    # let's request the url
    content = requests.get(fil_url)
    doc_content = content.json()

    for doc in doc_content['directory']['item']:
        doc_name = doc['name']
        doc_url = base_url + cik_num + fil_num + '/' + doc_name
        print(doc_url)
