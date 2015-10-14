#-*- coding: utf-8 -*-

from Crawler import *

crawler = Crawler()
crawler.query = raw_input("쿼리 : ")
output_type = raw_input("출력 타입 (phone / full) : ")
results = crawler.get(1)

data = open('data.txt', 'w')
for result in results:
    data.write(result.format(output_type))
data.close()
