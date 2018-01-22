# -*- coding:utf-8 -*- 
#!/usr/bin/env python

import os,re,pickle

class ParserBooklist():
    txtAddr = '1.txt'
    bookList = []
    nowCategory = 'root'
    def run(self):
        lastTotal = 1
        lastIsFile = False
        bookAttr = {'size': '', 'name': '', 'type': '', 'category': 'root'}
        categories = []
        typeList = ('zip', 'azw', '7z', 'txt', 'rsls', 'TXT', 'AZW3', 'azw3', 'mobi')
        with open(self.txtAddr,'r') as books:
            for book in books:
                book = book.strip()
                bookRegex = re.compile(r'(.*)\[(.*)\](.+)')
                bookAttrs = bookRegex.search(book.strip())
                categoryRegex = re.compile(r'\||`')
                categoryTotal = len(re.findall(categoryRegex, bookAttrs.group(1)))
                bookAttr['size'] = bookAttrs.group(2).strip()
                bookAttr['name'] = bookAttrs.group(3).strip()
                #按.拆分group3，弹出最后一个，如果在后缀名列表里面，则认为是文件（添加type），否则（把弹出的再添加进去）是目录
                filesplit = bookAttrs.group(3).strip().split('.')
                if len(filesplit) > 1 :
                    validateType = filesplit.pop()
                    if validateType in typeList:
                        isFile = True
                        bookAttr['type'] = validateType
                        bookAttr['name'] = '.'.join(filesplit)#将去掉后缀名的字符串重新组合成文件名
                    else:
                        isFile = False
                        filesplit.append(validateType)
                else:
                    isFile = False
                if categoryTotal == 1:
                    if isFile:
                        bookAttr['category'] = self.nowCategory
                    else:
                        bookAttr['category'] = 'root'
                        bookAttr['type'] = 'category'
                        self.nowCategory = 'root/' + bookAttr['name']
                else:
                    if (not lastIsFile and categoryTotal <= lastTotal) or (lastIsFile and not isFile and categoryTotal < lastTotal) or (lastIsFile and isFile and categoryTotal < lastTotal):#如果上一层是目录无论下一层是目录还是文件都需要剔除最后一个目录
                        categories = self.nowCategory.split('/', categoryTotal - 1)
                        categories.pop()
                    else:
                        categories = self.nowCategory.split('/')

                    if not isFile:
                        categories.append(bookAttrs.group(3).strip())
                        bookAttr['type'] = 'category'
                        bookAttr['name'] = '/'.join(categories)
                        self.nowCategory = bookAttr['name']
                    elif isFile and categoryTotal <= lastTotal:
                        bookAttr['category'] = '/'.join(categories)
                        self.nowCategory = bookAttr['category']
                    else:
                        #是文件，看当前的目录
                        bookAttr['category'] = self.nowCategory
                print(bookAttr)
                print('\n')
                self.bookList.append(bookAttr.copy())
                lastTotal = categoryTotal
                lastIsFile = isFile
        books = pickle.dumps(self.bookList)
        #print('\n'.join(self.bookList))

if __name__ == '__main__':
    parsertxt = ParserBooklist()
    parsertxt.run()