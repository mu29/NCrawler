#-*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
from Result import *

class Crawler:
    def __init__(self):
        self.base_url = 'http://openapi.naver.com/search?'
        self.key = '' # Naver API Key
        self.target = 'local'
        self.start = 1
        self.display = 100
        self.query = ''

    def get(self, start):
        if self.start > 1000:
            return []

        url = self.base_url
        url += 'key=' + self.key
        url += '&target=' + self.target
        url += '&start=' + str(self.start)
        url += '&display=' + str(self.display)
        url += '&query=' + self.query

        document = urllib.urlopen(url)
        soup = BeautifulSoup(document, 'lxml')
        results = []

        for item in soup.find_all('item'):
            title = item.contents[0].string
            phone = item.contents[4].string
            address = item.contents[5].string
            if phone is None:
                continue

            if phone[:3] != '010' and phone[:3] != '011':
                continue

            result = Result(title, phone, address)
            results.append(result)

        self.start += self.display
        return results + self.get(self.start)
