# -*- coding:utf-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash

from . import db

#数据库
class cximage(db.Model):
    __tablename__ = 'cximages'
    id = db.Column(db.Integer,primary_key = True,index=True)
    intro = db.Column(db.String(140))
    filename = db.Column(db.String(140),unique=True)
    time = db.Column(db.DateTime,nullable=False)
    #todo:添加外键关联到用户上，并且设置为索引
    #todo:添加用户表，包含姓名、班级、学号、微信OAuthID、ID

    def __repr__(self):
        return '<cximage {}>'.format(self.intro)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
        
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
