#encoding: utf-8
from flask import render_template
from . import main
from controller import Data
# import newRequest as ebd
from controller import app



data = Data.configData()

def stuff(key, cookies, website):
    format = 'json'
    load=ebd.Request()
    
    week = app.weeksEvents();

    rooms =  {i : ebd.INFO(week.get(i)).getRooms() for i in week}

    roomEvents = {i : ebd.INFO(week.get(i)).getEventsPerRoom() for i in week}
    
    eventInfo = {i : ebd.INFO(week.get(i)).getEventInfo() for i in week}
    
    return {'week':week, 'rooms':rooms, 'roomEvents':roomEvents, 'eventInfo':eventInfo}

# stuff = stuff(data['key'], data['cookie'], data['website'])
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
    
