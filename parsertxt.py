# -*- coding:utf-8 -*- 
#!/usr/bin/env python

import os,re,pickle

class ParserBooklist():
    txtAddr = '1.txt'
    bookList = []
    nowCategory = 'root'
    def run(self):
        lastTotal = 1
        bookAttr = {'size': '', 'name': '', 'type': '', 'category': 'root'}
        with open(self.txtAddr,'r') as books:
            for book in books:
                bookRegex = re.compile(r'(.*)\[(.*)\]([^\.]+)(\.(\w{3,4})$)?')
                bookAttrs = bookRegex.search(book.strip())
                categoryRegex = re.compile(r'\|')
                categoryTotal = len(re.findall(categoryRegex, bookAttrs.group(1)))
                bookAttr['size'] = bookAttrs.group(2)
                bookAttr['name'] = bookAttrs.group(3)
                if categoryTotal == 1:
                    if bookAttrs.group(4):
                        bookAttr['category'] = bookAttrs.group(3)
                    else:
                        bookAttr['category'] = 'root'
                else:
                    if categoryTotal <= lastTotal:
                        categories = self.nowCategory.split('/', categoryTotal - 1)
                        categories.pop()
                    if bookAttrs.group(4):
                        bookAttr['type'] = bookAttrs.group(5)
                    else:
                        categories.append(bookAttrs.group(3))
                        bookAttr['type'] = 'category'
                    bookAttr['category'] = '/'.join(categories)
                self.bookList.append(bookAttr)
                self.nowCategory = bookAttr['category']
                lastTotal = categoryTotal
        books = pickle.dumps(self.bookList)
        print(books)

if __name__ == '__main__':
    parsertxt = ParserBooklist()
    parsertxt.run()