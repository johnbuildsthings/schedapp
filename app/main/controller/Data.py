

def configData():
  title = "MAAWG35 October 2015"
  key = "a05ccb28175bd0ec495dea87e302e755"
  #key for june schedule just in case needed later for testing
  #key = '93c5b2c7d6a01f93c1fc704e6870ca9d'
  cookie = {'token': 's%3A128%3A%22pDL9ntrG9FoabtgR6QCB3haf8aQg2Ah40ovAJvqlESnt4jbdLGtNG17cQEVCvOcJsB3O7MWbAiNCprbpUo52CVReUN8bmna5tmWvDfnk8fOb1QArAKL1wbo02KOD98hn%22%3B'}
  website = "http://m3aawg35.sched.org/"

  date = {'Monday': 'October 19', 'Tuesday': 'October 20', 'Wednesday': 
    'October 21', 'Thursday': 'October 22', 'Friday': 'October 23'}

  Map = {'2015-10-19' : 'monday', '2015-10-20' : 'tuesday',
  '2015-10-21' : 'wednesday', '2015-10-22' : 'thursday', 
  '2015-10-23' : 'friday'}

  return{'title':title, 'key':key, 'cookie':cookie, 'website':website, 'date':date, 'Map':Map}
