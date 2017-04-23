# -*- coding: utf-8 -*-

"""
    blend of main and function, temporary.
"""

import requests
from bs4 import BeautifulSoup
import re
import time


def clean(text):
    """
        clean string
    """
    text = re.sub('^[^0-9]*', '', text)
    text = re.sub('s.*?d', 's d', text)
    text = re.sub('\\.*$', '', text)
    # text = re.sub('/\s\s+/g', ' ', text)
    text = re.sub('\*', ' ', text)
    text = re.sub('\n', ' ', text)
    text = re.sub('[ ]{2,}', ' ', text)
    return text


def getInfo(url):
    """
        get the html of the page containing the next departure time
    """
    r = requests.get(url)
    return r.content


def parserHtml(c):
    """
        get just the info we need from the html
    """
    soup = BeautifulSoup(c, 'html.parser')
    samples = soup.find_all('span', attrs={"class": u"inline-left"})
    return samples


while True:
    time.sleep(15)
    print(50*"\n")
    url = 'https://www.infotbm.com/nextdeparture/B/stoparea/TBT5529/backward'
    samples = parserHtml(getInfo(url))
    for tram in samples:
        print(clean(tram.text))
    print(1*"\n")
