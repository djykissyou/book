# -*- coding:utf-8 -*- 
#!/usr/bin/env python

import os
from app import create_app, db
from app.models import cximage
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
photos = UploadSet('PHOTO', IMAGES)
configure_uploads(app, photos)

def make_shell_context():
    return dict(app=app, db=db, cximage=cximage)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run() 
