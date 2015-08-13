#encoding: utf-8
from flask import render_template
from . import main
from controller import Data
# import newRequest as ebd
from controller import app



data = Data.configData()

stuff = app.weeksEvents()


@main.route('/')
def index():
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    week = stuff.get('week')
    rooms = stuff.get('rooms')
    roomEvents = stuff.get('roomEvents')
    eventInfo = stuff.get('eventInfo')
    title = data['title']
    date = data['date']
    
    return render_template('/Tmp2/basetmpTable.htm',
                            title=title,
                            days=days,
                            week=week,
                            date=date,
                            roomName=rooms,
                            roomEvents=roomEvents,
                            eventinfo=eventInfo)
    
