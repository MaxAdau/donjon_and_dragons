# coding: utf-8

from flask import Flask
import os

from models import db

# Create Flask app
app = Flask(__name__)

# Define postgresql config
POSTGRES = {
    'user': 'lsmpiaeycofhbv',
    'pw': '2e21b7e80e8548b0badd911dae1397ed5d39efd9e56d71b4a8d29131c86c4cb4',
    'db': 'd9ujtmrcjsae3i',
    'host': 'ec2-54-247-177-33.eu-west-1.compute.amazonaws.com',
    'port': '5432'
}

# Setup Flask app to reach postgresql base
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DB_USER:PASSWORD@HOST/DATABASE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['DEBUG'] = True

# Connect SQLAlchemy object with Flask applicatoin
db.init_app(app)


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

