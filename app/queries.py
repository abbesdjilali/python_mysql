from typing import List, Dict
from datetime import date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, Float, Integer, String, ForeignKey, func, text
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.dialects.mysql import DATETIME
import logging
import os



db_user = os.getenv('MYSQL_USER')
db_pwd = os.getenv('MYSQL_PASSWORD')
db_host = os.getenv('MYSQL_HOST')
db_port = os.getenv('MYSQL_PORT')
db_name = os.getenv('MYSQL_DATABASE')

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'


# CONNECTION
engine = create_engine(connection_str)
connection = engine.connect()
logging.info('Connection with mysql successfuly...\n')

metadata = MetaData(bind=engine)
metadata.reflect(only=['customers', 'employees', 'offices',
                 'orderdetails', 'orders', 'payments', 'productlines', 'products'])


# mapping of metadata
Base = automap_base(metadata=metadata)
Base.prepare()
payments = Base.classes.payments;
Employees = Base.classes.employees;


Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


def show_tables() -> List:
    tab = []
    for table in metadata.sorted_tables:
        tab.append(table.name)
    return tab


def countEmployess():
    result = [];
    # result = connection.execute(text("select count(*) count from employees"))
    count = session.query(func.count(Employees.employeeNumber))
    for n in count:
        result.append(n)
    return result
