from flask_mongoengine import MongoEngine


db = MongoEngine()

class HealthyCheck(db.Document):
    status_code = db.IntField()
    date = db.StringField()

    def to_json(self):
        return {
            'status': self.status_code,
            'date': self.date
        }