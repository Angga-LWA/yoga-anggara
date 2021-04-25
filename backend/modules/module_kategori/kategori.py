import json
import datetime
import sys
import os
import bcrypt

import urllib
import requests
import mysql.connector

from flask import Flask
from flask import request
from flask import session
from flask import make_response
from flask import redirect
from flask import url_for
from flask import jsonify

from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity


from marshmallow_sqlalchemy import ModelSchema
from marshmallow            import fields

sys.path.append("core")
sys.path.append("core/models")
sys.path.append("core/settings")

from models     import *
from settings   import *

class get:
    def __init__(self):
        pass

    def get_data_all(self):
        response = {
                        "message"       : {},
                        "data"          : {}
                   }
        try:
            list = []

            get_data = Kategori.query.all()
            kategori_schema = KategoriSchema(many=True)
            kategori = kategori_schema.dump(get_data)

                response["message"]         = 'Success'
                response["data"]            = kategori

                return make_response(json.dumps(response)), 200

            except:

                response["message"]     = 'Failed'
                response["data"]        = ""

                return make_response(json.dumps(response)), 400

        def get_data_one(self):
            response = {
                            "message"       : {},
                            "data"          : {}
                       }
            try:
                idnya = str(request.json.get('id'))

                get_data    = Kategori.query.get(idnya)
                kategori_schema = KategoriSchema()
                kategori    = kategori_schema.dump(get_data)

                response["message"]     = 'Success'
                response["data"]        = kategori

                return make_response(json.dumps(response)), 200

            except:

                response["message"]     = 'Failed'
                response["data"]        = ""

                return make_response(json.dumps(response)), 400

class post:
    def __init__(self):
        pass

    def 
