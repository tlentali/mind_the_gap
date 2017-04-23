# -*- coding: utf-8 -*-

"""
    functions to :
    - clean
    - get url
    - parse html
"""

import requests
from bs4 import BeautifulSoup
import re


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
