# -*- coding:utf-8 -*-
#!/usr/bin/env python

import os,re,string
from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:fenjin-99@localhost/book?charset=utf8')
DBSession = sessionmaker(bind=engine)
rootdir = '/media/daijinyong/移动硬盘/kindle电子书/'
book = {'size': '', 'name': '', 'type': '', 'category': 'root'}
bookList = []
NULL = 0

class Books(BaseModel):
    __tablename__ = 'books'  # 表名
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    book_name = Column(CHAR(600), nullable=False)
    book_type = Column(VARCHAR(4), default='mobi', nullable=False)
    book_size = Column(VARCHAR(9))
    book_category = Column(CHAR(120))

def init_db():
    '''
    初始化数据库
    :return:
    '''
    BaseModel.metadata.create_all(engine)

def traverseD(dir):
    list = os.listdir(dir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        path = os.path.join(dir,list[i])
        if os.path.isfile(path):
            book['size'] = size2mk(path)
            (book['name'],book['type']) = os.path.splitext(list[i])
            book['type'] = book['type'].lstrip('.')
            book['category'] = dir.replace(rootdir, "", 1)
            bookList.append(book.copy())
        elif os.path.isdir(path):
            traverseD(path)

def size2mk(path):
    if os.path.isfile(path):
        orgSize = os.path.getsize(path)
        kSize = orgSize/1024
        if round(kSize,2) <= 1024:
            return str(round(kSize,2)) + 'KB'
        else:
            return str(round(kSize/1024,2)) + 'MB'

def addBook():
    session = DBSession()
    for ABook in bookList:
        bookNeedAdd = Books(id = NULL,
                            book_name = ABook['name'],
                            book_type = ABook['type'],
                            book_size = ABook['size'],
                            book_category = ABook['category'])
        session.add(bookNeedAdd)
        session.commit()

if __name__ == '__main__':
    init_db()
    traverseD(rootdir)
    addBook()