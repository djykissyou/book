# -*- coding:utf-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash

from . import db

#数据库
class student(db.Model):
    __tablename__ = 'studentinfo'
    id = db.Column(db.Integer, primary_key = True, index=True, autoincrement=True)
    xingming = db.Column(db.String(6),unique=True,nullable=False)
    shenfenzheng = db.Column(db.String(18),unique=True,nullable=False)
    kahao = db.Column(db.String(20),unique=True,nullable=False)
    banji = db.Column(db.Enum(u'14w1', u'14w2', u'14w3'))
    xuexiao = db.Column(db.String(255),nullable=False)
    zhuanye = db.Column(db.String(255))
    yuke = db.Column(db.Boolean)
    dianhua = db.Column(db.String(11), nullable=False)
    time = db.Column(db.DateTime,nullable=False)
    #todo:添加外键关联到用户上，并且设置为索引
    #todo:添加用户表，包含姓名、班级、学号、微信OAuthID、ID

    def __repr__(self):
        return '<student {}>'.format(self.intro)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
        
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
