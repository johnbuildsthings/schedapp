import retrieveData
import parseData
import getColor
import parseEventInfo

    
def update():
  retrieveData.Request('app/data/jsonDump.json')
  getColor.getColors(retrieveData.read('app/data/jsonDump.json'))

def weeksEvents():
  
  data = retrieveData.read('app/data/jsonDump.json')

  Monday = parseData.Day('monday', data)
  Tuesday = parseData.Day('tuesday', data)
  Wednesday = parseData.Day('wednesday', data)
  Thursday = parseData.Day('thursday', data)
  Friday = parseData.Day('friday', data)

  week = {'Monday': Monday, 'Tuesday': Tuesday, 'Wednesday': Wednesday, 
  'Thursday': Thursday, 'Friday': Friday}

  rooms =  {i : parseEventInfo.Info(week.get(i)).getRooms() for i in week}

  roomEvents = {i : parseEventInfo.Info(week.get(i)).getEventsPerRoom() for i in week}
  
  eventInfo = {i : parseEventInfo.Info(week.get(i)).getEventInfo() for i in week}
    
  return {'week':week, 'rooms':rooms, 'roomEvents':roomEvents, 'eventInfo':eventInfo}


