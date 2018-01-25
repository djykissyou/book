# -*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Required
from manage import photos

#表单
class CXForm(Form):
    xingming = TextAreaField(u'姓名', validators=[Required()])
    shenfenzheng = TextAreaField(u'身份证号', validators=[Required()])
    kahao = TextAreaField(u'银行卡号', validators=[Required()])
    xuexiao = TextAreaField(u'当前就读大学', validators=[Required()])
    dianhua = TextAreaField(u'联系电话', validators=[Required()])

    submit = SubmitField('Submit')
