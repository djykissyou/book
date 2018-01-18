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
                bookRegex = re.compile(r'(.*)\[(.)*\](.)+(\.(\w{3,4}))?')
                bookAttrs = bookRegex.search(book.strip())
                categoryRegex = re.compile(r'\|')
                categoryTotal = len(re.findall(categoryRegex, bookAttrs[0]))
                bookAttr['size'] = bookAttrs[1]
                bookAttr['name'] = bookAttrs[2]
                if categoryTotal == 1:
                    if bookAttrs[3]:
                        bookAttr['category'] = bookAttrs[2]
                    else:
                        bookAttr['category'] = 'root'
                else:
                    if categoryTotal <= lastTotal:
                        categories = self.nowCategory.split('/', categoryTotal - 1)
                        categories.pop()
                    if bookAttrs[3]:
                        bookAttr['type'] = bookAttrs[4]
                    else:
                        categories.append(bookAttrs[2])
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
