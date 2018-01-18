# -*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Required
from manage import photos

#表单
class CXForm(Form):
    intro = TextAreaField(u'诚信行为介绍', validators=[Required()])
    photo = FileField(u'诚信图片', validators=[
        FileRequired(),
        FileAllowed(['jpg','png','jpeg','gif','mp4'], u'目前仅能上传图片')
    ])
    submit = SubmitField('Submit')
