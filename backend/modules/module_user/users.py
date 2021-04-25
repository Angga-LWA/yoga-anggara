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

    def get_user_all(self):
        response = {
                        "message"      : {},
                        "data"         : {}

                   }
        try:
            list = []

            get_user = User.query.all()
            user_schema = UserSchema(many=True)
            user = user_schema.dump(get_user)

            response["message"]     = 'Success'
            response["data"]        = user

            return make_response(json.dumps(response)), 200

        except:

            response["message"]     = 'Failed'
            response["data"]        = ""

            return make_response(json.dumps(response)), 400

    def get_user_one(self):
        response = {
                        "message"      : {},
                        "data"         : {}
                   }
        try:
            idnya = str(request.json.get('id'))

            get_user    = User.query.get(idnya)
            user_schema = UserSchema()
            user        = user_schema.dump(get_user)

            response["message"]     = 'Success'
            response["data"]        = user

            return make_response(json.dumps(response)), 200

        except:

            response["message"]     = 'Failed'
            response["data"]        = ""

            return make_response(json.dumps(response)), 400

class post:
    def __init__(self):
        pass

    def login(self):
        response = {
                        "message"      : {},
                        "data"         : {}
                   }
        try:
            username = request.json.get('username', None)
            password = request.json.get('password', None)

            if not username:
                response["message"]     = 'Failed! Missing Username!'
                response["data"]        = "Error"

                return make_response(json.dumps(response)), 400
            if not password:
                response["message"]     = 'Failed! Missing Password!'
                response["data"]        = "Error"

                return make_response(json.dumps(response)), 400



            user    = User.query.filter_by(username=username, password=password).first()

            if not user:
                response["message"]     = 'Failed! Username Not Found / Password Wrong!'
                response["data"]        = "Error"

                return make_response(json.dumps(response)), 404


            waktunya = datetime.datetime.now()

            user.last_login = waktunya

            db.session.commit()


            hashed  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            if bcrypt.checkpw(password.encode('utf-8'), hashed):

                expires = datetime.timedelta(minutes=60)
                access_token = create_access_token(identity={"username": username}, expires_delta=expires)

                response["message"]     = 'Success'
                response["data"]        = access_token

                return make_response(json.dumps(response)), 200

            else:
                response["message"]     = 'Failed! Invalid Login Info!'
                response["data"]        = "Error"

                return make_response(json.dumps(response)), 400

        except AttributeError:
            return 'Provide an Username and Password in JSON format in the request body', 400

    def create_user(self):
        response = {
                        "message"      : {},
                        "data"         : {}
                   }

        try:
            username_in = request.json.get('username_in')
            username    = request.json.get('username')
            password    = request.json.get('password')
            nama        = request.json.get('nama')
            tgl_lahir   = request.json.get('tgl_lahir')
            jen_kel     = request.json.get('jen_kel')
            no_tlp      = request.json.get('no_tlp')
            role_id     = request.json.get('role_id')
            email_user  = request.json.get('email')

            tgl_lahir   = datetime.datetime.strptime(tgl_lahir, '%d-%m-%Y')

            get_user    = User.query.filter_by(username=username).first()
            if get_user is not None:
                response["message"]     = 'Failed'
                response["data"]        = 'Username Already Exist!'
                return make_response(json.dumps(response)), 400

            get_email    = User.query.filter_by(email_user=email_user).first()
            if get_email is not None:
                response["message"]     = 'Failed'
                response["data"]        = 'Email Already Exist!'
                return make_response(json.dumps(response)), 400

            user = User(username=username, password=password, nama=nama, tgl_lahir=tgl_lahir, jen_kel=jen_kel, no_tlp=no_tlp, role_id=role_id, email_user=email_user)
            db.session.add(user)
            db.session.commit()

            tgl_log = datetime.datetime.now()
            log = 'Menambahkan Data Admin Terbaru'

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


class delete:
    def __init__(self):
        pass
    def delete_user(self):
        response = {
                        "message"      : {},
                        "data"         : {}
                   }

        try:
            idnya = str(request.json.get('id'))

            get_user = User.query.filter_by(id_user=idnya).delete()

            db.session.commit()
            db.session.execute("ALTER TABLE User AUTO_INCREMENT=0")

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
    def update_user(self):
        response = {
                        "message"      : {},
                        "data"         : {}
                   }
        try:
            id_user     = str(request.json.get('id_user'))
            username_in = request.json.get('username_in')
            username    = request.json.get('username')
            password    = request.json.get('password')
            nama        = request.json.get('nama')
            tgl_lahir   = request.json.get('tgl_lahir')
            jen_kel     = request.json.get('jen_kel')
            no_tlp      = request.json.get('no_tlp')
            role_id     = request.json.get('role_id')
            email_user  = request.json.get('email')

            tgl_lahir   = datetime.datetime.strptime(tgl_lahir, '%d-%m-%Y')

            get_user    = User.query.get(id_user)

            get_user.username_in = username_in
            get_user.username    = username
            get_user.password    = password
            get_user.nama        = nama
            get_user.tgl_lahir   = tgl_lahir
            get_user.jen_kel     = jen_kel
            get_user.no_tlp      = no_tlp
            get_user.role_id     = role_id
            get_user.email_user  = email_user

            db.session.commit()

            user_schema = UserSchema()
            user        = user_schema.dump(get_user)

            response["message"]     = 'Success'
            response["data"]        = "data berhasil diupdate"

            return make_response(json.dumps(response)), 200

        except:

            response["message"]     = 'Failed'
            response["data"]        = ""

            return make_response(json.dumps(response)), 400
