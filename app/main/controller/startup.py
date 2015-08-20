import retrieveData
import getColor

def update():
  retrieveData.Request('app/data/jsonDump.json')
  getColor.getColors(retrieveData.read('app/data/jsonDump.json'))

if __name__ == '__main__':
  update()