#!/usr/bin/env python
from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, env

env.hosts = ['sched.drkurt.com']

env.user = 'ec2-user'

def prepare_deploy():
	local("gunicorn manage:app")
	
def webServerUpdate():
	code_dir = '/home/ec2-user/m3aawgApp.git/app'
	run("source venv/bin/activate")
	run("pkill gunicorn")
	run("gunicorn manage:app")

def updateApp():
	local("git add --all && git commit -m 'auto update'")
	local("git push web master")
	
def deploy():
	code_dir = '/home/ec2-user/m3aawgApp.git/app'
	updateApp()
	with cd(code_dir):
		run("source venv/bin/activate")
		run("pkill gunicorn")
		run("sudo pip install -r requirements.txt")
		run("gunicorn manage:app")

def startServer():
	code_dir = '/home/ec2-user/m3aawgApp.git/app'	
	with cd(code_dir):
		run("source venv/bin/activate")
		run("gunicorn manage:app")
