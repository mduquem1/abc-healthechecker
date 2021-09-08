from flask import Flask

def create_app(config): 
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'health_checker',
        'host': 'localhost',
        'port': 27017,
        'username': 'health_checker',
        'password': 'rootpassword',
        'authentication_source': 'admin'
    }

    return app