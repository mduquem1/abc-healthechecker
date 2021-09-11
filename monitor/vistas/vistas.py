from monitor.modelos.modelos import Notifier
from flask import jsonify
from flask_restful import Resource
import requests
from datetime import datetime
from ..modelos import db, HealthyCheck

class VistaHealthyChecker(Resource):
    def get(self):
        # url = ''
        # response = requests.get(url)
        nuevo_check = HealthyCheck(status='success', date="{}".format(datetime.utcnow()))
        nuevo_check.save()
        return nuevo_check.to_json()

    def post(self):
        notifier = Notifier()
        notifier.send_error_notification('Reportes', 500, 'Error with Reportes clinica API')