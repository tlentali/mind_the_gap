import collections
import re
import requests
from bs4 import BeautifulSoup

TbmInfo = collections.namedtuple('TbmInfo', ('duration', 'direction'))


class TbmParser:
    __slots__ = ('url', 'content', 'info')

    def __init__(self, url):
        """
        :type url: str
        """
        self.url = url
        self.content = None
        self.info = []

    def load_page(self):
        page = requests.get(self.url)
        self.content = page.content

    def extract_info(self):
        self.info.clear()
        soup = BeautifulSoup(self.content, 'html.parser')
        all = soup.find_all('span', attrs={"class": u"inline-left"})
        regex = re.compile(r'^\s+(\d+).*?direction\s*(.*?)$', re.DOTALL)

        for info in all:
            line = regex.findall(info.text)[0]
            self.info.append(TbmInfo(duration=line[0], direction=line[1].strip()))

    def parse(self):
        self.load_page()
        self.extract_info()
