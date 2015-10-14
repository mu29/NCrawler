#-*- coding: utf-8 -*-

class Result:
    def __init__(self, title, phone, address):
        self.title = title.encode('utf-8')
        self.phone = phone.encode('utf-8')
        self.address = address.encode('utf-8')
        self.title = self.title.replace('<b>', '')
        self.title = self.title.replace('</b>', '')

    def format(self, output_type):
        if output_type == 'phone':
            return self.phone + '\n'
        else:
            return self.title + ' : ' + self.phone + ' (' + self.address + ')\n'
