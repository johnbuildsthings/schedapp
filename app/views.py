#encoding: utf-8
from flask import render_template
from app import app
import newRequest as ebd

@app.route('/')
@app.route('/index')
def index():
    days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    date = {'Monday': 'February 16', 'Tuesday': 'February 17', 'Wednesday': 
    'February 18', 'Thursday': 'February 19', 'Friday': 'February 20'}
    
    format = 'json'
    key = ''
    load=ebd.Request(key, format)
    cookies = {}
    
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
    
    
    return render_template('/Tmp2/basetmpTable.htm',
                            days = days,
                            week=week,
                            date=date,
                            roomName=rooms,
                            roomEvents=roomEvents,
                            eventinfo=eventInfo)
    