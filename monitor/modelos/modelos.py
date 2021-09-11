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
        url = 'http://127.0.0.1:5001/notify'
        myobj = {'api': api,'status_code': status_code,'description': description,'smtp_password': 'here-is-the-password'}
        requests.post(url, json = myobj)