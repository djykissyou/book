# -*- coding:utf-8 -*-

from werkzeug.utils import secure_filename
from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import CXForm
from .. import db
from ..models import cximage
from manage import photos

@main.route('/', methods=['GET', 'POST'])
def index():
    form = CXForm()
    if form.validate_on_submit():
        filename = form.photo.data.filename
	#todo:添加对文件的安全性验证
        #filename = secure_filename(form.photo.data.filename)
        imagefile = photos.save(form.photo.data , name=filename)
        intro = cximage(intro=form.intro.data, filename=imagefile,time=datetime.now())
        db.session.add(intro)
        return redirect(url_for('.index'))
	#return "good"
    else:
        return render_template('index.html',
            form=form, current_time=datetime.utcnow())
