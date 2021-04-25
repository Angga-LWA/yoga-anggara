from flask import Flask, request
import bcrypt, jwt, datetime, urllib
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datatest.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/posdb'
# params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=DESKTOP-EDUF2AV\SQLEXPRESS;DATABASE=mydata;Trusted_Connection=yes;')
# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'igUGIG73H(HD@(YS(Sh9hd20XHS)U@)#*)$&&DVB'
jwt = JWTManager(app)
