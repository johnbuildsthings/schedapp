#encoding: utf-8
from flask import render_template
from . import main
import newRequest as ebd


def stuff(key, cookie):
    format = 'json'
    load=ebd.Request(key, format)
    
    Monday = ebd.Day('monday', load)
    Tuesday = ebd.Day('tuesday', load)
    Wednesday = ebd.Day('wednesday', load)
    Thursday = ebd.Day('thursday', load)
    Friday = ebd.Day('friday', load)
    
    week={'Monday': Monday, 'Tuesday': Tuesday, 'Wednesday': Wednesday, 
    'Thursday': Thursday, 'Friday': Friday}

    rooms =  {i : ebd.INFO(week.get(i), cookie=cookies ).getRooms() for i in week}

    roomEvents = {i : ebd.INFO(week.get(i), cookie=cookies).getEventsPerRoom() for i in week}
    
    eventInfo = {i : ebd.INFO(week.get(i), cookie=cookies).getEventInfo() for i in week}
    
    return {'week':week, 'rooms':rooms, 'roomEvents':roomEvents, 'eventInfo':eventInfo}
    
key = ''
cookie = {}    
stuff = stuff(key, cookie)


@main.route('/')
def index():
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    date = {'Monday': 'February 16', 'Tuesday': 'February 17', 'Wednesday': 
    'February 18', 'Thursday': 'February 19', 'Friday': 'February 20'}
    week = stuff.get('week')
    rooms = stuff.get('rooms')
    roomEvents = stuff.get('roomEvents')
    eventInfo = stuff.get('eventInfo')
    
    return render_template('/Tmp2/basetmpTable.htm',
                            days = days,
                            week=week,
                            date=date,
                            roomName=rooms,
                            roomEvents=roomEvents,
                            eventinfo=eventInfo)
    
