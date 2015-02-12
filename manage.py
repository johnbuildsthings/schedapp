#!/usr/bin/env python
import os
from app import create_app
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app)
manager.add_command("shell", Shell(make_context=make_shell_context))

if os.path.exists('.env'):
    print ('Importing environment from .env...')
    for line in open('.env'):
        var = line.split().split('=')
        if len(var)==2:
            os.environ[var[0]] = var[1]
if __name__=='__main__':
    manager.run()