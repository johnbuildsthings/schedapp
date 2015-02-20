# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import re
import requests
import urllib
import json



def Request(key, format, website):
    params = {'api_key': key, 'format': format}
    data = urllib.urlencode(params)
    url = (website)
    api_req = url + 'api/event/list?' + data
    
    req = requests.get(api_req)
    apiResponse = req.text
    if format == 'json':
        load = json.loads(apiResponse)
    else:
        raise ValueError('unexpected request format')    
    return load



class Day(object):
    
    def __init__(self, day, info):
        self.day=day
        self.info=info
        self.daysEvents=[]
        self.getInfo()
        self.numEvents=len(self.daysEvents)
    
    
    def findDay(self, infoLine):
        Map = {'2015-02-16' : 'monday', '2015-02-17' : 'tuesday',
'2015-02-18' : 'wednesday', '2015-02-19' : 'thursday', 
'2015-02-20' : 'friday'}
        start = infoLine[u'event_start']
        date = start.split(' ')[0]
        return Map.get(date)
    
    def getInfo(self):
        wantedInfo = ['name', 'eventStart', 'eventEnd','day', 'venue', 'event_type', 'description']
        
        for line in self.info:
            if self.day == self.findDay(line):
                infoDict = {}
                for w in wantedInfo:
                    try:
                        infoDict[w]=(line[w])
                    except KeyError:
                        if w == 'eventStart':
                            start = (line['event_start'].split(' '))
                            infoDict[w]=start[1]
                        elif w == 'eventEnd':
                            end = (line['event_end'].split(' '))
                            infoDict[w]=end[1]
                        elif w == 'day':
                            infoDict[w]=self.day
                        else:
                            infoDict[w]='No info available'
                self.daysEvents.append(infoDict)
                
            else:
                continue
    



class INFO(object):
  
    def __init__(self, day, cookie=None):
        self.day = day.daysEvents
        self.rooms = []
        self.roomEvents = {}
        self.eventInfo = {} 
        self.cookies = cookie 
    
    
    def cleanData(self, description):
        description = description
        unwanted = ['&hellip;', '&ldquo;', '&omicron;', "~", '&nbsp']
        space = {'&nbsp;': ' ', '&rsquo;': "'", '&ndash;': "-",
        '&amp;': "&", '&rdquo;': "'", '\\u0418': 'N', '\\u02ba': '"',
        '\\r\\n': ' '}
        
        for key in space:
            description = description.replace(key, space[key])
        for un in unwanted:
            description = description.replace(un, '')
        ##cleans unwanted html tags out of the description
        while description.find('<') >= 0:
            l = description.find('<')
            g = description.find('>')
            description = description[:l]+description[g+1:]
        return description    
    
    def Rooms(self):
        for event in self.day:
            room = self.cleanData(str(event['venue'])).strip()
            if room in self.rooms:
                continue
            else:
                self.rooms.append(room)
        
    def getRooms(self):
        self.Rooms()
        return sorted(self.rooms)
    
    
    
    def EventsPerRoom(self):               
        for room in self.rooms:
            self.roomEvents[room] = [] 
        
        for event in self.day:
            ##print event
            eventName = event['name']
            ##print eventName
            start = event['eventStart']
            ##start = start.split(' ')
            self.eventInfo[eventName] = []##sets up for the eventinfo function
            room = self.cleanData(event['venue'])
            self.roomEvents[str(room).strip()].append([start, eventName])
        
        for key in self.roomEvents:
            self.roomEvents[key]=sorted(self.roomEvents.get(key))
            events =[]
            for event in self.roomEvents.get(key):
                events.append(event[1])
                self.roomEvents[key]=events
        
        
    def getEventsPerRoom(self):
        self.Rooms()
        self.EventsPerRoom()
        return self.roomEvents
        
    
    def editTime(self, start, end):
        """returns the pixel values for start and the height
        of the time box... must be in string with am or pm"""
        sP = int()
        hP = int()
        time_to_pixel = {'14:30:00': '51.15', '09:00:00': '13.64',
'12:00:00': '34.10', '07:00:00': '0.0', '11:30:00': '30.68',
'10:00:00': '20.46', '17:00:00': '68.20', '09:30:00': '17.05',
'08:00:00': '6.82', '08:30:00': '10.23', '12:30:00': '37.51',
'07:30:00': '3.41', '13:30:00': '44.33', '11:00:00': '27.28', 
'10:30:00': '23.87', '15:30:00': '57.97', '16:00:00': '61.38', 
'16:30:00': '64.79', '13:00:00': '40.92', '14:00:00': '47.74',
'18:00:00': '75.02', '15:00:00': '54.56', '17:30:00': '71.61'}
        
        try:
            sP = float(time_to_pixel.get(start))
            eP = float(time_to_pixel.get(end))
            hP = eP - sP
        except TypeError:
            if int(start[3:5])==15 or int(end[3:5])==15:
                new = '00'
                start = start[0:3]+new+start[5:]
                end = end[0:3]+new+end[5:]
                return self.editTime(start, end)
                
            elif int(start[3:5])==45 or int(end[3:5])==45:
                new = int(start[0:2])+1
                start = str(new)+'00'+start[5:]
                newE = int(end[0:2])
                end = str(newE)+'30'+end[5:]
                sP = int(time_to_pixel.get(start))
                eP = int(time_to_pixel.get(end))
        return [sP, hP]    
           
    def soup(self):
        url = ("https://m3aawg33.sched.org/grid-full")
        cookie = self.cookies
        resp = requests.post(url, cookies=cookie)
        soup = BeautifulSoup(resp.content)
        return soup
    
    def findEventColor(self, event, soup):
        """case sensative... event must be a string of the 
        event title"""
        event = soup.find("strong", text=re.compile(event))
        colorDiv = event.parent.parent.parent
        attr = colorDiv['style'].split(';')
        attr = attr[0].split(':')
    
        return attr[1]
        
    def EventInfo(self):
        soup = self.soup()
        for event in self.day:
            name = event['name']
            eventType =  event['event_type']
            try:
                color = self.findEventColor(name, soup)
            except AttributeError:
                if "Administrative & Maintenance" in eventType:
                    color = '#fa1e37'
                else:
                    color = '#ffa00a'
            start = event['eventStart']
            end = event['eventEnd']
            time = self.editTime(start, end)
            if int(start[:2]) >= 18:
               time = (71.59, 3.41)
            day = event['day']
            
            description = self.cleanData(event['description'])
            nesInfo = [name, day, time[0], time[1],start,end, description, color]
            for i in nesInfo:
                self.eventInfo[name].append(i)
        
    def getEventInfo(self):
        self.Rooms()
        self.EventsPerRoom()
        self.EventInfo()
        return self.eventInfo
        
'''
if __name__ == '__main__':
    format = 'json'
    key = ''
    cookie = {}
    website = "http://m3aawg33.sched.org/"
    load=Request(key, format, website)
    wednesday=Day('wednesday', load)
    ##print wednesday.daysEvents
    info = INFO(wednesday, cookie = cookie)
    ##print info.getRooms()
    ##print info.getEventsPerRoom()
    print info.getEventInfo().get('M3AAWG Night Out')    
'''