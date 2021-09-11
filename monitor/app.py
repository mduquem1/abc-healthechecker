from datetime import datetime
import requests
from flask_restful import Api
from flask_apscheduler import APScheduler
from monitor import create_app
from .modelos import db,HealthyCheck, Notifier

app = create_app('default')
app_context = app.app_context()
app_context.push()


db.init_app(app)
api = Api(app)

def do_healthcheck():
    url = 'http://127.0.0.1:5000/reportes/healthcheck'
    # response = requests.get(url)
    try:
        response = requests.get(url)
        nuevo_check = HealthyCheck(status_code=response.status_code, date="{}".format(datetime.utcnow()))
        nuevo_check.save()
        return response.status_code       
    except requests.exceptions.HTTPError as err:
        nuevo_check = HealthyCheck(status_code=err.response.status_code, date="{}".format(datetime.utcnow()))
        nuevo_check.save()
        notifier = Notifier()
        notifier.send_error_notification('Reportes', err.response.status_code, err.response.reason)
        return err.response.status_code

scheduler = APScheduler()
scheduler.add_job(id = 'Do a health check to reports', func = do_healthcheck, trigger = 'interval', seconds = 300)
scheduler.start()

