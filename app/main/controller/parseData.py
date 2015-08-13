import Data
data = Data.configData()

class Day(object):
    
  def __init__(self, day, info):
    self.day=day
    self.info=info
    self.daysEvents=[]
    self.getInfo()
    self.numEvents=len(self.daysEvents)
  
    
  def findDay(self, infoLine):
    Map = data['Map']
        
    start = infoLine[u'event_start']
    date = start.split(' ')[0]
    return Map.get(date)
  
  def getInfo(self):
    wantedInfo = ['name', 'eventStart', 'eventEnd', 'day', 'venue', 'event_type', 'description']
    
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