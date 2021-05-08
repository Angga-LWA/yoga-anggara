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

class put:
    def __init__(self):
        pass
    def update_discount(self):
        response = {
                        "message"       : {},
                        "data"          : {}
                   }
        try:
            id_discount         = str(request.json.get('id_discount'))
            nama_discount       = request.json.get('nama_discount')
            tgl_disc_berlaku    = request.json.get('tgl_disc_berlaku')
            tgl_disc_berakhir   = request.json.get('tgl_disc_berakhir')
            tgl_disc            = request.json.get('tgl_disc')
            flag_disc           = request.json.get('flag_disc')
            kode_disc           = request.json.get('kode_disc')
            role_disc_1         = request.json.get('role_disc_1')
            role_disc_2         = request.json.get('role_disc_2')
            role_disc_3         = request.json.get('role_disc_3')
            keterangan_disc     = request.json.get('keterangan_disc')

            tgl_disc_berlaku = datetime.datetime.strptime(tgl_disc_berlaku, '%d-%m-%Y')
            tgl_disc_berakhir = datetime.datetime.strptime(tgl_disc_berakhir, '%d-%m-%Y')
            tgl_disc = datetime.datetime.strptime(tgl_disc, '%d-%m-%Y')

            get_discount = Discount.query.get(id_discount)

            get_discount.nama_discount      = nama_discount
            get_discount.tgl_disc_berlaku   = tgl_disc_berlaku
            get_discount.tgl_disc_berakhir  = tgl_disc_berakhir
            get_discount.tgl_disc           = tgl_disc
            get_discount.flag_disc          = flag_disc
            get_discount.kode_disc          = kode_disc
            get_discount.role_disc_1        = role_disc_1
            get_discount.role_disc_2        = role_disc_2
            get_discount.role_disc_3        = role_disc_3
            get_discount.keterangan_disc    = keterangan_disc

            db.session.commit()

            discount_schema = DiscountSchema()
            discount        = discount_schema.dump(get_discount)

            response["message"]     = 'Success'
            response["data"]        = "data berhasil di update"

            return make_response(json.dumps(response)), 200

        except:

            response["message"]     = 'Failed'
            response["data"]        = ""

            return make_response(json.dumps(response)), 400

class post:
    def __init__(self):
        pass

    def create_discount(self):
        response = {
                        "message"       : {},
                        "data"          : {}
                   }
        try:
            nama_discount       = request.json.get('nama_discount')
            tgl_disc_berlaku    = request.json.get('tgl_disc_berlaku')
            tgl_disc_berakhir   = request.json.get('tgl_disc_berakhir')
            tgl_disc            = request.json.get('tgl_disc')
            flag_disc           = request.json.get('flag_disc')
            kode_disc           = request.json.get('kode_disc')
            role_disc_1         = request.json.get('role_disc_1')
            role_disc_2         = request.json.get('role_disc_2')
            role_disc_3         = request.json.get('role_disc_3')
            keterangan_disc     = request.json.get('keterangan_disc')

            tgl_disc_berlaku = datetime.datetime.strptime(tgl_disc_berlaku, '%d-%m-%Y')
            tgl_disc_berakhir = datetime.datetime.strptime(tgl_disc_berakhir, '%d-%m-%Y')
            tgl_disc = datetime.datetime.strptime(tgl_disc, '%d-%m-%Y')
