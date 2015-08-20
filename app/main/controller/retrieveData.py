import sys, os
import urllib
import requests
import time
import json
import Data


def makePath(realtivePath):
  return os.path.join(os.path.dirname(__file__), os.path.realpath(realtivePath))


def write(data, filename):
  dumpFile = makePath(filename)
  with open(dumpFile, 'w') as f:
    json.dump(data, f, ensure_ascii=False)

def read(filename):
  dumpFile = makePath(filename)
  with open(dumpFile) as json_file:
    info = json.load(json_file)
    json_file.close()
    return json.loads(info)

def Request(dumpFile):
  data = Data.configData()
  key = data['key']
  format = 'json'
  website = data['website']

  params = {'api_key': key, 'format': format}
  data = urllib.urlencode(params)
  url = (website)
  api_req = url + 'api/event/list?' + data
 
  try:
    response = requests.get(api_req)  
  except requests.exceptions.ConnectionError as e:
    print 'trying again in 30 seconds'
    time.sleep(60)
    print 'trying again now'
    response = requests.get(api_req)
  
  apiResponse = response.text
  File = makePath(dumpFile)
  write(apiResponse, File)

##===========unit test of bad connection============
"""
def connection_error():
    raise requests.expections.ConnectionError

class TestSuitabilityFunction(object):
    def test_connection_error(self):
        requests.get = MagicMock(side_effect=connection_error)
        with self.assertRaises(requests.expections.ConnectionError) as cm:
            resp = Request('93c5b2c7d6a01f93c1fc704e6870ca9d', 'json', "http://m3aawg34.sched.org/")
            exception = cm.exception

t = TestSuitabilityFunction()
t.test_connection_error()
"""
##==============end test=============================


