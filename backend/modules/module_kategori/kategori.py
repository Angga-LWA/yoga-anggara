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

                get_data = Kategori.query.get(idnya)
                kategori_schema = KategoriSchema()
                kategori = kategori_schema.dump(get_data)

                response["message"]     = 'Success'
                response["data"]        = kategori

                return make_response(json.dumps(response)), 200

            except:

                response["message"]     = 'Failed'
                response["data"]        = ""

                return make_response(json.dumps(response)), 400

 class delete:
    def __init__(self):
        pass
    def delete_data(self):
        response = {
                        "message"       : {},
                        "data"          : {}
                   }

        try:
            idnya = str(request.json.get('id'))

            get_data = Kategori.query.filter_by(id_kategori=idnya).delete()

            db.session.commit()
            db.session.execute("ALTER TABLE Kategori AUTO_INCREMENT=0")

            response["message"]     = 'Success'
            response["data"]        = "data berhasil dihapus"

            return make_response(json.dumps(response)), 200

        except:

            response["message"]     = 'Failed'
            response["data"]        = ""

            return make_response(json.dumps(response)), 400

class put:
    def __init__(self):
        pass
    def update_data(self):
        response = {
                        "message"       : {},
                        "data"          : {}
                   }
        try:
            id_kategori   = str(request.json.get(id_kategori))
            nama_kategori = request.json.get('nama_kategori')
            tgl_kategori  = request.json.get('tgl_kategori')
            flag_kategori = request.json.get('flag_kategori')

            tgl_kategori  = datetime.datetime.strptime(tgl_kategori, '%d-%m-%Y')

            get_data      = Kategori.query.get(id_kategori)

            get_data.nama_kategori  = nama_kategori
            get_data.tgl_kategori   = tgl_kategori
            get_data.flag_kategori  = flag_kategori

            db.session.commit()

            kategori_schema = KategoriSchema()
            kategori        = kategori_schema.dump(get_data)

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

    def add_data(self):
        response = {
                        "message"       : {},
                        "data"          : {}
                   }
        try:
            nama_kategori = request.json.get('nama_kategori')
            tgl_kategori  = request.json.get('tgl_kategori')
            flag_kategori = request.json.get('flag_kategori')

            tgl_kategori  = datetime.datetime.strptime(tgl_kategori, '%d-%m-%Y')

            get_data      = Kategori.query.filter_by(nama_kategori=nama_kategori).first()
            if get_data is not None:
                response["message"]     = 'Failed'
                response["data"]        = 'Nama Kategori Already Exist!'
                return make_response(json.dumps(response)), 400

            kategori = Kategori(nama_kategori=nama_kategori, tgl_kategori=tgl_kategori, flag_kategori=flag_kategori)
            db.session.add(kategori)
            db.session.commit()

            tgl_log = datetime.datetime.now()
            log = 'Menambahkan Data Kategori Terbaru'

            log = Log(tgl_log=tgl_log, log=log, username_in=username_in)
            db.session.add(log)
            db.session.commit()

            response["message"]     = 'Success'
            response["data"]        = "data berhasil masuk"

            return make_response(json.dumps(response)), 200

        except:

            response["message"]     = 'Failed'
            response["data"]        = "Error"

            return make_response(json.dumps(response)), 400
