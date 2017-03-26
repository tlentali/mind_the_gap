
import requests
from bs4 import BeautifulSoup
import re

def clean(text):
    """
        clean string
    """
    text = re.sub('^[^0-9]*', '', text)
    text = re.sub('/\s\s+/g', ' ', text)
    text = re.sub('s.*?d', 's d', text)
    text = re.sub('\\.*$', '', text)
    return text


r = requests.get\
    ('https://www.infotbm.com/nextdeparture/B/stoparea/TBT5529/backward')

c = r.content
soup = BeautifulSoup(c, 'html.parser')
samples = soup.find_all('span', attrs={"class": u"inline-left"})

for tram in samples:
    print(clean(tram.text))
