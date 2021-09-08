from monitor.vistas.vistas import VistaHealthyChecker
from flask_restful import Api
from flask_apscheduler import APScheduler
from monitor import create_app
from .modelos import db

app = create_app('default')
app_context = app.app_context()
app_context.push()


db.init_app(app)
api = Api(app)

api.add_resource(VistaHealthyChecker, '/monitor')

if __name__ == "__main__":
    scheduler = APScheduler()
    scheduler.add_job(id = 'Description of cron job', func = VistaHealthyChecker, trigger = 'interval', seconds = 10)
    scheduler.start()

