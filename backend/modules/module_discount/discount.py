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

    def get_discount_all(self):
        response = {
                        "message"       : {},
                        "data"          : {}
                   }
        try:
            list = []

            get_discount = Discount.query.all()
            discount_schema = DiscountSchema(many=True)
            discount = discount_schema.dump(get_discount)

            response["message"]         = 'Success'
            response["data"]            = discount

            return make_response(json.dumps(response)), 200

        except:

            response["message"]         = 'Failed'
            response["data"]            = ""

            return make_response(json.dumps(response)), 400

    def get_discount_one(self):
        response = {
                            "message"       : {},
                            "data"          : {}
                   }
        try:
            idnya = str(request.json.get('id'))

            get_discount = Discount.query.get(idnya)
            discount_schema = DiscountSchema()
            discount = discount_schema.dump(get_discount)

            response["message"]     = 'Success'
            response["data"]        = discount

            return make_response(json.dumps(response)), 200

        except:

            response["message"]     = 'Failed'
            response["data"]        = ""

            return make_response(json.dumps(response)), 400

class delete:
    def __init__(self):
        pass
    def delete_discount(self):
        response = {
                        "message"       : {},
                        "data"          : {}
                   }

        try:
            idnya  str(request.json.get('id'))

            get_discount = Discount.query.filter_by(id_discount=idnya).delete()

            db.session.commit()
            db.session.execute("ALTER TABLE Discount AUTO_INCREMENT=0")

            response["message"]         = 'Success'
            response["data"]            = "data berhasil dihapus"

            return make_response(json.dumps(response)), 200

        except:

            response["message"]     = 'Failed'
            response["data"]        = ""

            return make_response(json.dumps(response)), 400
