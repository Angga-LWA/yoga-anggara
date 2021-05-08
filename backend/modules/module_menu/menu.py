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

            get_data = Menu.query.all()
            menu_schema = MenuSchema(many=True)
            menu = menu_schema.dump(get_data)

                response["message"]         = 'Success'
                response["data"]            = menu

                return make_response(json.dumps(response)), 200

        except:

            response["message"]         = 'Failed'
            response["data"]            = ""

            return make_response(json.dumps(response)), 400

    def get_data_one(self):
        response = {
                        "message"       : {},
                        "data"          : {}
                   }
        try:
            idnya = str(request.json.get('id'))

            get_data = Menu.query.get(idnya)
            menu_schema = MenuSchema()
            menu = menu_schema.dump(get_data)

            response["message"]     = 'Success'
            response["data"]        = menu

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

            get data = Menu.query.filter_by(id_menu=idnya).delete()

            db.session.commit()
            db.session.execute("ALTER TABLE Menu AUTO_INCREMENT=0")

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
            id_menu     = str(request.json.get('id_menu'))
            nama_menu   = request.json.get('nama_menu')
            tgl_menu    = request.json.get('tgl_menu')
            harga_menu  = request.json.get('harga_menu')
            flag_menu   = request.json.get('flag_menu')
            image_menu  = request.json.get('image_menu')
            qty_menu    = request.json.get('qty_menu')

            tgl_menu    = datetime.datetime.strptime(tgl_menu, '%d-%m-%Y')

            get_data    = Menu.query.get(id_menu)

            get_data.nama_menu  = nama_menu
            get_data.tgl_menu   = tgl_menu
            get_data.harga_menu = harga_menu
            get_data.flag_menu  = flag_menu
            get_data.image_menu = image_menu
            get_data.qty_menu   = qty_menu

            db.session.commit()

            menu_schema = MenuSchema()
            menu        = menu_schema.dump(get_data)

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
            nama_menu   = request.json.get('nama_menu')
            tgl_menu    = request.json.get('tgl_menu')
            harga_menu  = request.json.get('harga_menu')
            flag_menu   = request.json.get('flag_menu')
            image_menu  = request.json.get('image_menu')
            qty_menu    = request.json.get('qty_menu')

            tgl_menu    = datetime.datetime.strptime(tgl_menu, '%d-%m-%Y')

            get_menu    = Menu.query.filter_by(nama_menu=nama_menu).first()
            if get_menu is not None:
                response["message"]     = 'Failed'
                response["data"]        = 'Nama Menu Already Exist!'
                return make_response(json.dumps(response)), 400

            get_qty     = Menu.query.filter_by(qty_menu=qty_menu).first()
            if get_qty is not None:
                response["message"]     = 'Failed'
                response["data"]        = 'Jumlah Quantity Already Exist!'
                return make_response(json.dumps(response)), 400

            menu = Menu(nama_menu=nama_menu, tgl_menu=tgl_menu, harga_menu=harga_menu, flag_menu=flag_menu, image_menu=image_menu, qty_menu=qty_menu)
            db.session.add(menu)
            db.session.commit()

            tgl_log = datetime.datetime.now()
            log = 'Menambahkan Data Menu Terbaru'

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
