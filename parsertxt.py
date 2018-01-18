# -*- coding:utf-8 -*- 
#!/usr/bin/env python

import os
class ParserBooklist():
    txtAddr = '1.txt'
    def run(self):
        with open(self.txtAddr,'r') as books:
            for book in books:
                print(book.strip())

if __name__ == '__main__':
    parsertxt = ParserBooklist()
    parsertxt.run()
