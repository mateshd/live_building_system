from sqlite3 import Timestamp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask("Live Building System")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/fake_meter.sqlite'

#ORM
db = SQLAlchemy(app)
print(db)

# create meters table
class Meters(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    label = db.Column( db.String(50) )

    def __init__(self,label):
        self.label = label

# creae meters data table
class Meters_data(db.Model):
    id = db.Column( db.Integer , primary_key=True )
    meter_id = db.Column( db.Integer , db.ForeignKey('meters.id') )
    timestamp = db.Column( db.DateTime , default=datetime.now())
    value = db.Column( db.Integer)

    def __init__(self,meter_id,value):
        self.meter_id = meter_id
        self.value = value


db.create_all()

# Create data in Meters Table 
"""
eca = Meters('ECA EDMI Mk7C E1c Meter')
db.session.add(eca)
db.session.commit()"""

# create data in Metres Data Table
"""ams_data = Meters_data(1,7000)
db.session.add(ams_data)
db.session.commit()
"""
