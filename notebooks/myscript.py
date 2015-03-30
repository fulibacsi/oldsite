# encode: utf-8

import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://kozbeszerzes.ceu.hu'
kozgep_suburl = '/entity/t/10950676.xml'

# create a function, and get the needed information out of the xml
def get_tenders(base_url, sub_url):
    response = requests.get(base_url + sub_url)
    if not response.status_code == 200:
        print 'Download failed!'
    else:
        won_tenders = [['Year', 'Value', 'Desc']] # init with headers
        soup = BeautifulSoup(response.content)
        for tender in soup.find('all_tenders_won').findAll('tender'):
            tender_response = requests.get(base_url + tender['url'])
            if not tender_response.status_code == 200:
                print 'Tender download failed!'
            else:
                tender_soup = BeautifulSoup(tender_response.content)
                won_tenders.append([
                    tender_soup.find('tender')['year'],
                    tender_soup.find('tender')['estimated_value'],
                    '"' + tender_soup.find('tender')['subject'] + '"' # we use " to make sure that the data is wrapped
                ])
        return won_tenders

# write a save function
# since we have hungarian text, we need to encode our characters in UTF-8
# and unfortunately csv module does not support that
import codecs
def save_results(filename, tenders):
    with codecs.open(filename, 'w', 'utf-8') as output:
        for tender in tenders:
            output.write(u';'.join(tender) + u'\n')

# write a main function
def main():
    save_results('kozgep.csv', get_tenders(BASE_URL, kozgep_suburl))

if __name__ == '__main__':
    main()
