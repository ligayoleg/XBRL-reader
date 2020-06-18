# import libraries
import requests
import urllib
from bs4 import BeautifulSoup

# function to build url


def make_url(base_url, comp):
    url = base_url
    # add each component to the base url
    for r in comp:
        url = '{}/{}'.format(url, r)

    return url


# define base url
base_url = r"https://www.sec.gov/Archives/edgar/daily-index"

# define cik
cik_num = '/21344/'

# define year
year = '2019'

# define extension
ext = 'index.json'

# create year url
year_url = make_url(base_url, [year, ext])

# request year url
content = requests.get(year_url)
year_content = content.json()


# loop through year content
for item in year_content['directory']['item']:

    # get the name of the folder
    print('-' * 100)
    print("Pulling url for quarter {}".format(item['name']))

    # create Q url
    qtr_url = make_url(base_url, [year, item['name'], ext])

    file_content = requests.get(qtr_url)
    qtr_dec_content = file_content.json()

    print(qtr_dec_content['directory']['name'])
    print('-'*100)
    print('Pulling Files:')

    for fname in qtr_dec_content['directory']['item']:
        # find only files that have 'master' in them
        if "master" in fname['name']:

            # file url
            file_url = make_url(base_url, [year, item['name'], fname['name']])
            # print(file_url)

            # print('-'*100)
            # print('PullingData:')


fileUrl = r"https://www.sec.gov/Archives/edgar/daily-index/2019/QTR4/master.20191213.idx"
content = requests.get(fileUrl).content

# lets write content of idx to txt
with open('master-20191212.txt', 'wb') as f:
    f.write(content)

# lets read content of txt filef
with open('master-20191212.txt', 'rb') as f:
    bData = f.read()

# decode
data = bData.decode('utf-8').split(' ')

for index, item in enumerate(data):

    if 'ftp://ftp.sec.gov/edgar/' in item:
        start_ind = index

# create list to remove the junk
data_format = data[start_ind + 1:]

master_data = []

# loop through the data list
for index, item in enumerate(data_format):

    if index == 0:
        clean_item_data = item.replace('\n', '^').split("^")
        clean_item_data = clean_item_data[8:]
    else:
        clean_item_data = item.replace('\n', '^').split('^')
        print("Item: => " + item)
        print("DATA: => ")
        print(clean_item_data)


# for index, row in enumerate(clean_item_data):
#     # when you find a text file
#     if '.txt' in row:
#         mini_list = clean_item_data[(index - 4): index+1]
#         print(mini_list)
