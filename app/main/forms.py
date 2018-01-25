# -*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired
from manage import photos

#表单
class CXForm(Form):
    xingming = StringField(u'姓名', [DataRequired()])
    shenfenzheng = StringField(u'身份证号', [DataRequired()])
    kahao = StringField(u'银行卡号', [DataRequired()])
    banji = SelectField(u'毕业所在班级', choices=[('14w1', u'14微机一班'), ('14w2', u'14微机二班'), ('14w3', u'14微机三班')])
    xuexiao = StringField(u'当前就读大学(已工作则填工作单位)', [DataRequired()])
    zhuanye = StringField(u'大学所学专业（已工作则填岗位）')
    yuke = BooleanField(u'大学预科请在此选项打钩')
    dianhua = StringField(u'联系电话', [DataRequired()])

    submit = SubmitField(u'提交')
