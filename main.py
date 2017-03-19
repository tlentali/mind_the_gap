
import requests
from bs4 import BeautifulSoup
import re


r = requests.get\
    ('https://www.infotbm.com/nextdeparture/B/stoparea/TBT5529/backward')

c = r.content
soup = BeautifulSoup(c, 'html.parser')

samples = soup.find_all('span', attrs={"class": u"inline-left"})

for tram in samples:
    depart = tram.text
    depart = re.sub('^[^0-9]*', '', depart)
    depart = re.sub('/\s\s+/g', ' ', depart)
    depart = re.sub('s.*?d', 's d', depart)
    depart = re.sub('\\.*$', '', depart)
    print(depart)
