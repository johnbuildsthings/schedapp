from bs4 import BeautifulSoup
import re
import requests
import Data
import retrieveData
import json

data = Data.configData();

def Soup():
  url = (data['website']+"/grid-full")
  cookie = data['cookie']
  resp = requests.post(url, cookies=cookie)
  soup = BeautifulSoup(resp.content)
  return soup

def findEventColor(event, soup):
  """case sensative... event must be a string of the 
  event title"""
  event = soup.find("strong", text=re.compile(event))
  colorDiv = event.parent.parent.parent
  attr = colorDiv['style'].split(';')
  attr = attr[0].split(':')

  return attr[1]


def getColors(events):
  eventType = {}
  soup = Soup();

  for event in events:
    name = event['name']
    Type = event['event_type']
    try:
      color = findEventColor(name, soup)
    except AttributeError:
      color = '#ffffff'
    eventType[Type] = color

  retrieveData.write(json.dumps(eventType), '../../data/colors.json')

# events = retrieveData.read('app/data/jsonDump.json')
# getColors(events)