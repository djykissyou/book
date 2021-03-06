# -*- coding:utf-8 -*-

from werkzeug.utils import secure_filename
from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import CXForm
from .. import db
from ..models import student
from manage import photos

@main.route('/', methods=['GET', 'POST'])
def index():
    form = CXForm()
    if form.validate_on_submit():
        intro = student(xingming=form.xingming.data,
                        shenfenzheng=form.shenfenzheng.data,
                        kahao=form.kahao.data, banji=form.banji.data,
                        xuexiao=form.xuexiao.data, zhuanye=form.zhuanye.data,
                        yuke=form.yuke.data,
                        dianhua=form.dianhua.data,
                        time=datetime.now())
        db.session.add(intro)
        return redirect(url_for('.ok'))
	#return "good"
    else:
        return render_template('index.html',
            form=form, current_time=datetime.utcnow())

@main.route('/ok/')
def ok():
    return render_template('ok.html')