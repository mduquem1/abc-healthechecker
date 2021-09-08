from flask_mongoengine import MongoEngine


db = MongoEngine()

class HealthyCheck(db.Document):
    status = db.StringField()
    date = db.StringField()

    def to_json(self):
        return {
            'status': self.status,
            'date': self.date
        }