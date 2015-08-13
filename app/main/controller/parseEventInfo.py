# -*- coding: UTF-8 -*-
import retrieveData


class Info(object):
  
  def __init__(self, day):
    self.day = day.daysEvents
    self.rooms = []
    self.roomEvents = {}
    self.eventInfo = {} 
    self.colors = retrieveData.read('app/data/colors.json')
    
    
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
    sP = float()
    hP = float()
    start = start
    end = end
    time_to_pixel = {'14:30:00': '51.15', '09:00:00': '13.64',
'12:00:00': '34.10', '07:00:00': '0.0', '11:30:00': '30.68',
'10:00:00': '20.46', '17:00:00': '68.20', '09:30:00': '17.05',
'08:00:00': '6.82', '08:30:00': '10.23', '12:30:00': '37.51',
'07:30:00': '3.41', '13:30:00': '44.33', '11:00:00': '27.28', 
'10:30:00': '23.87', '15:30:00': '57.97', '16:00:00': '61.38', 
'16:30:00': '64.79', '13:00:00': '40.92', '14:00:00': '47.74',
'18:00:00': '75.02', '15:00:00': '54.56', '17:30:00': '71.61', 
'18:30:00': '78.43', '19:00:00': '81.84'}
    
    try:
      sP = float(time_to_pixel.get(start))
    except TypeError:
      if '45' in start:
        new = int(start[0:2])
        start = str(new)+':30'+start[5:]
      else:
        new = '00'
        start = start[0:3]+new+start[5:]
      sP = float(time_to_pixel.get(start))
    try:
      eP = float(time_to_pixel.get(end))
    except TypeError:
      if '45' in end:
        newE = int(end[0:2])+1
        end = str(newE)+':00'+end[5:]
      else:
        new = '00'
        end = end[0:3]+new+end[5:]
      eP = float(time_to_pixel.get(end))
    hP = round(eP - sP, 4)
    
    return [sP, hP]    
           
      
  def EventInfo(self):
    for event in self.day:
      name = event['name']
      Type = event['event_type']

      try:
        color = self.colors[Type]
        if(color == 'no color'):
          color = '#ffffff'
      except AttributeError:
        color = '#ffffff'
      start = event['eventStart']
      end = event['eventEnd']
      try:
        if int(end[:2]) >= 19:
          end = '18:30:00'
        try:
          time = self.editTime(start, end)
        except TypeError:
          pass
      except ValueError:
        start = "08:00:00"
        end = "09:00:00"
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
        

# if __name__ == '__main__':
#   # print data
#   load=Request()

  # wednesday=Day('wednesday', load)
  # ##print wednesday.daysEvents
  # info = INFO(wednesday, website, cookie = cookie)
  # ##print info.getRooms()
  # ##print info.getEventsPerRoom()
  # print info.getEventInfo() 

