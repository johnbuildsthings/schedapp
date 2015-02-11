import eventBreakDown as ebd
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

monday = ebd.INFO('/home/john/htmlTest/html/apiMonday.csv')
tuesday = ebd.INFO('/home/john/htmlTest/html/apiTuesday.csv')
wednesday = ebd.INFO('/home/john/htmlTest/html/apiWednesday.csv')
thursday = ebd.INFO('/home/john/htmlTest/html/apiThursday.csv')
friday = ebd.INFO('/home/john/htmlTest/html/apiFriday.csv')
##info = ebd.INFO()
week={'monday':monday, 'tuesday':tuesday, 'wednesday':wednesday, 'thursday':thursday, 'friday':friday}

rooms =  {i : week.get(i).getRooms() for i in week}
##print rooms
roomEvents = {i : week.get(i).getEventsPerRoom() for i in week}
##print roomEvents
eventInfo = {i : week.get(i).getEventInfo() for i in week}