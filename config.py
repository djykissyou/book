# -*- coding:utf-8 -*-

import os
from flask_uploads import IMAGES, ALL
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    #在shell中使用下列命令设置环境变量
    #export MAIL_USERNAME = your_username
    #export MAIL_PASSWORD = your_password
    #export MAIL_SENDER = your_email_sender
    #export MAIL_RECEIVER = your_email_receiver
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SENDER = os.environ.get('MAIL_SENDER')
    MAIL_RECEIVER = os.environ.get('MAIL_RECEIVER')
    MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or 'Flasky_Admin'

    UPLOADED_PHOTO_DEST = os.path.dirname(os.path.abspath(__file__))
    UPLOADED_PHOTO_ALLOW = IMAGES

    @staticmethod    
    def init_app(app):
        pass

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'mysql://studentinfo:fenjin-99@localhost:3306/studentinfo'

config = {
    'production': ProductionConfig,

    'default': ProductionConfig
} 
