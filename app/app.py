from datetime import date
from sqlalchemy.orm import sessionmaker
from typing import List, Dict
from flask import Flask, jsonify

import json
from sqlalchemy import create_engine, MetaData, Table, Column, Float, Integer, String, ForeignKey
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.dialects.mysql import DATETIME
import logging
import os
import queries as queries

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


# db_user = os.getenv('MYSQL_USER')
# db_pwd = os.getenv('MYSQL_PASSWORD')
# db_host = os.getenv('MYSQL_HOST')
# db_port = os.getenv('MYSQL_PORT')
# db_name = os.getenv('MYSQL_DATABASE')

# connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'


# # CONNECTION
# engine = create_engine(connection_str)
# connection = engine.connect()
# logging.info('Connection with mysql successfuly...\n')

# metadata = MetaData(bind=engine)
# metadata.reflect(only=['customers', 'employees', 'offices',
#                  'orderdetails', 'orders', 'payments', 'productlines', 'products'])


# # mapping of metadata
# Base = automap_base(metadata=metadata)
# Base.prepare()
# payments = Base.classes.payments


# Session = sessionmaker()
# Session.configure(bind=engine)
# session = Session()


@app.route('/')
def index() -> str:
    return ' CONNECTION OF Python_MySQL_APP WITH Database test'


@app.route('/tables')
def tables() -> str:
    return json.dumps({'Tables of database ': queries.show_tables()})


@app.route('/countEmployees')
def employeesCount() -> str:
    return jsonify(queries.countEmployess());


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
