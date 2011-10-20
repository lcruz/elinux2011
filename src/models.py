from google.appengine.ext import db

class Data(db.Model):
    code = db.StringProperty()
    title = db.StringProperty()
    has_child = db.BooleanProperty()
   

