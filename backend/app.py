import json
import time
import sys
import os

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

sys.path.append("modules")
sys.path.append("module_user")
sys.path.append("core")
sys.path.append("core/models")
sys.path.append("core/settings")


from module_user import users

from settings import *
from models import *


############## LOGIN GET TOKEN  ###################

@app.route('/login', methods=['POST'])
def login():
    log = users.post().login()
    return log

###### ADMIN (HANYA BISA DIAKSES OLEH SUPER ADMIN) #######
@app.route('/v1/web/adminone', methods=['GET'])
@jwt_required
def admincrud():
    y = users.get().get_user_one()
    return y

@app.route('/v1/web/adminall', methods=['GET'])
@jwt_required
def adminall():
    y = users.get().get_user_all()
    return y

@app.route('/v1/web/adminadd', methods=['POST'])
@jwt_required
def adminadd():
    y = users.post().create_user()
    return y

@app.route('/v1/web/admindelete', methods=['DELETE'])
@jwt_required
def admindelete():
    y = users.delete().delete_user()
    return y

@app.route('/v1/web/adminupdate', methods=['PUT'])
@jwt_required
def adminupdate():
    y = users.put().update_user()
    return y
#
# ###### MENU #######
# @app.route('/v1/web/menuone', methods=['GET'])
# @jwt_required
# def menuone():
#     y = menu_api.get().get_data_one()
#     return y
#
# @app.route('/v1/web/menuall', methods=['GET'])
# @jwt_required
# def menuall():
#     y = menu_api.get().get_data_all()
#     return y
#
# @app.route('/v1/web/menuadd', methods=['POST'])
# @jwt_required
# def menuadd():
#     y = menu_api.post().add_data()
#     return y
#
# @app.route('/v1/web/menudelete', methods=['DELETE'])
# @jwt_required
# def menudelete():
#     y = menu_api.delete().delete_data()
#     return y
#
# @app.route('/v1/web/menuupdate', methods=['PUT'])
# @jwt_required
# def menuupdate():
#     y = menu_api.put().update_data()
#     return y
#
# ###### KATEGORI #######
#
# @app.route('/v1/web/kategorione', methods=['GET'])
# @jwt_required
# def kategorione():
#     y = kategori_api.get().get_data_one()
#     return y
#
# @app.route('/v1/web/kategoriall', methods=['GET'])
# @jwt_required
# def kategoriall():
#     y = kategori_api.get().get_data_all()
#     return y
#
# @app.route('/v1/web/kategoriadd', methods=['POST'])
# @jwt_required
# def kategoriadd():
#     y = kategori_api.post().add_data()
#     return y
#
# @app.route('/v1/web/kategoridelete', methods=['DELETE'])
# @jwt_required
# def kategoridelete():
#     y = kategori_api.delete().delete_data()
#     return y
#
# @app.route('/v1/web/kategoriupdate', methods=['PUT'])
# @jwt_required
# def kategoriupdate():
#     y = kategori_api.put().update_data()
#     return y

# ###### DISCOUNT ###########
@app.route('/v1/web/discountone', methods=['GET'])
@jwt_required
def discountone():
    y = discount_api.get().get_discount_one()
    return y

app.route('/v1/web/discountall', methods=['GET'])
@jwt_required
def discountall():
    y = discount_api.get().get_discount_all()
    return y

@app.route('/v1/web/discountadd', methods=['POST'])
@jwt_required
def discountadd():
    y = discount_api.post().create_discount()
    return y

@app.route('/v1/web/discountdelete', methods=['DELETE'])
@jwt_required
def discountdelete():
    y = discounts_api.delete().delete_discount()
    return y

@app.route('/v1/web/discountupdate', methods=['PUT'])
@jwt_required
def discountupdate():
    y = discount_api.put().update_discount()
    return y


######## MEMBER ###########
@app.route('/v1/web/memberone', methods=['GET'])
@jwt_required
def memberone():
    y = member_api.get().get_member_one()
    return y

app.route('/v1/web/memberall', methods=['GET'])
@jwt_required
def memberall():
    y = member_api.get().get_member_all()
    return y

@app.route('/v1/web/memberadd', methods=['POST'])
@jwt_required
def memberadd():
    y = member_api.post().create_member()
    return y

@app.route('/v1/web/memberdelete', methods=['DELETE'])
@jwt_required
def memberdelete():
    y = member_api.delete().delete_member()
    return y

@app.route('/v1/web/memberupdate', methods=['PUT'])
@jwt_required
def memberupdate():
    y = member_api.put().update_member()
    return y

############# TRANSAKSI ############################
@app.route('/v1/web/transaksione', methods=['GET'])
@jwt_required
def transaksione():
    y = transaksi_api.get().get_transaksi_one()
    return y

app.route('/v1/web/transaksiall', methods=['GET'])
@jwt_required
def transaksiall():
    y = transaksi_api.get().get_transaski_all()
    return y

@app.route('/v1/web/transaksiadd', methods=['POST'])
@jwt_required
def transaksiadd():
    y = transaksi_api.post().create_transaksi()
    return y

@app.route('/v1/web/transaskidelete', methods=['DELETE'])
@jwt_required
def transaksidelete():
    y = transaksi_api.delete().delete_transaksi()
    return y

@app.route('/v1/web/transaksiupdate', methods=['PUT'])
@jwt_required
def transaksiupdate():
    y = transaksi_api.put().update_transaksi()
    return y

############# LOG #################
@app.route('/v1/web/logone', methods=['GET'])
@jwt_required
def logone():
    y = log_api.get().get_log_one()
    return y

app.route('/v1/web/logall', methods=['GET'])
@jwt_required
def logall():
    y = log_api.get().get_log_all()
    return y

@app.route('/v1/web/logadd', methods=['POST'])
@jwt_required
def logadd():
    y = log_api.post().create_log()
    return y

@app.route('/v1/web/logdelete', methods=['DELETE'])
@jwt_required
def logdelete():
    y = log_api.delete().delete_log()
    return y

@app.route('/v1/web/logupdate', methods=['PUT'])
@jwt_required
def logupdate():
    y = log_api.put().update_log()
    return y

############# ROLE #################
@app.route('/v1/web/roleone', methods=['GET'])
@jwt_required
def roleone():
    y = role_api.get().get_role_one()
    return y

app.route('/v1/web/roleall', methods=['GET'])
@jwt_required
def roleall():
    y = role_api.get().get_role_all()
    return y

@app.route('/v1/web/roleadd', methods=['POST'])
@jwt_required
def roleadd():
    y = role_api.post().create_role()
    return y

@app.route('/v1/web/roledelete', methods=['DELETE'])
@jwt_required
def roledelete():
    y = role_api.delete().delete_role()
    return y

@app.route('/v1/web/roleupdate', methods=['PUT'])
@jwt_required
def roleupdate():
    y = role_api.put().update_role()
    return y

app.run(debug=True, port=10000)
