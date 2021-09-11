from flask_mongoengine import MongoEngine
import requests

db = MongoEngine()

class HealthyCheck(db.Document):
    status_code = db.IntField()
    date = db.StringField()

    def to_json(self):
        return {
            'status': self.status_code,
            'date': self.date
        }

class Notifier():
    def send_error_notification(self, api, status_code, description):
        url = 'http://127.0.0.1:5000/notify'
        myobj = {'api': api,'status_code': status_code,'description': description,'smtp_password': '6478088dc1f65dcebbb31fc186f47142-fa6e84b7-2009bf3e'}
        requests.post(url, json = myobj)