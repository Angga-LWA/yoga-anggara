import sys
import os
import datetime

from flask_sqlalchemy import SQLAlchemy

from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from settings import *

db = SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    __tablename__ = 'User'
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    nama = db.Column(db.Text, nullable=False)
    tgl_lahir = db.Column(db.Date, nullable=False)
    jen_kel = db.Column(db.Text, nullable=False)
    no_tlp = db.Column(db.Text, nullable=False)
    role_id = db.Column(db.Text, nullable=False)
    email_user = db.Column(db.Text, unique=True, nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)

class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = db.session
    id_user = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    nama = fields.String(required=True)
    tgl_lahir = fields.Date(required=True)
    jen_kel = fields.String(required=True)
    no_tlp = fields.String(required=True)
    role_id = fields.String(required=True)
    email_user = fields.String(required=True)
    last_login = fields.DateTime(required=True)

##################################################################
class Role(db.Model):
    __tablename__ = 'Role'
    id_role = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Text, unique=True, nullable=False)

class RoleSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Role
        sqla_session = db.session
    id_role = fields.Integer(dump_only=True)
    role = fields.String(required=True)

####################################################################
class Kategori(db.Model):
    __tablename__ = 'Kategori'
    id_kategori = db.Column(db.Integer, primary_key=True)
    nama_kategori = db.Column(db.Text, unique=True, nullable=False)
    tgl_kategori = db.Column(db.Date, nullable=False)
    flag_kategori = db.Column(db.Text, nullable=False)

class KategoriSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Kategori
        sqla_session = db.session
    id_kategori = fields.Integer(dump_only=True)
    nama_kategori = fields.String(required=True)
    tgl_kategori = fields.Date(required=True)
    flag_kategori = fields.String(required=True)

##################################################################
class Menu(db.Model):
    __tablename__ = 'Menu'
    id_menu = db.Column(db.Integer, primary_key=True)
    nama_menu = db.Column(db.Text, unique=True, nullable=False)
    tgl_menu = db.Column(db.Date, nullable=False)
    harga_menu = db.Column(db.Integer, nullable=False)
    flag_menu = db.Column(db.Text, nullable=False)
    image_menu = db.Column(db.Text, nullable=False)
    qty_menu = db.Column(db.Integer, nullable=False)

class MenuSchema(ModelSchema):
    class Meta(ModelSchema):
        model = Menu
        sqla_session = db.session
    id_menu = fields.Integer(dump_only=True)
    nama_menu = fields.String(required=True)
    tgl_menu = fields.Date(required=True)
    harga_menu = fields.String(required=True)
    flag_menu = fields.String(required=True)
    image_menu = fields.String(required=True)
    qty_menu = fields.Integer(required=True)

###################################################################
class Discount(db.Model):
    __tablename__ = 'Discount'
    id_discount = db.Column(db.Integer, primary_key=True)
    nama_discount = db.Column(db.Text, unique=True, nullable=False)
    tgl_disc_berlaku = db.Column(db.Date, nullable=False)
    tgl_disc_berakhir = db.Column(db.Date, nullable=False)
    tgl_disc = db.Column(db.Date, nullable=False)
    flag_disc = db.Column(db.Text, nullable=False)
    kode_disc = db.Column(db.Text, nullable=False)
    role_disc_1 = db.Column(db.Text, nullable=False)
    role_disc_2 = db.Column(db.Text, nullable=False)
    role_disc_3 = db.Column(db.Text, nullable=False)
    keterangan_disc = db.Column(db.Text, nullable=False)

class DiscountSchema(ModelSchema):
    class Meta(ModelSchema):
        model = Discount
        sqla_session = db.session
    id_discount = fields.Integer(dump_only=True)
    nama_discount = fields.String(required=True)
    tgl_disc_berlaku = fields.Date(required=True)
    tgl_disc_berakhir = fields.Date(required=True)
    tgl_disc = fields.Date(required=True)
    flag_disc = fields.String(required=True)
    kode_disc = fields.String(required=True)
    role_disc_1 = fields.String(required=True)
    role_disc_2 = fields.String(required=True)
    role_disc_3 = fields.String(required=True)
    keterangan_disc = fields.String(required=True)

##################################################################
class Member(db.Model):
    __tablename__ = 'Member'
    id_member = db.Column(db.Integer, primary_key=True)
    nama_member = db.Column(db.Text, unique=True, nullable=False)
    tgl_lahir_member = db.Column(db.Date, nullable=False)
    no_tlp_member = db.Column(db.Text, nullable=False)
    email_member = db.Column(db.Text, nullable=False)
    tgl_buat_member = db.Column(db.Date, nullable=False)
    flag_member = db.Column(db.Text, nullable=False)

class MemberSchema(ModelSchema):
    class Meta(ModelSchema):
        model = Member
        sqla_session = db.session
    id_member = fields.Integer(dump_only=True)
    nama_member = fields.String(required=True)
    tgl_lahir_member = fields.Date(required=True)
    no_tlp_member = fields.String(required=True)
    email_member = fields.String(required=True)
    tgl_buat_member = fields.Date(required=True)
    flag_member = fields.String(required=True)

###################################################################
class Transaksi(db.Model):
    __tablename__ = 'Transaksi'
    id_transaksi = db.Column(db.Integer, primary_key=True)
    tgl_transaksi = db.Column(db.Date, nullable=False)
    item_transaksi = db.Column(db.Text, nullable=False)
    harga_transaksi = db.Column(db.Text, nullable=False)
    qty_transaksi = db.Column(db.Text, nullable=False)
    total_transaksi = db.Column(db.Text, nullable=False)
    flag_transaksi = db.Column(db.Text, nullable=False)
    discount_transaksi = db.Column(db.Text, nullable=False)
    member_discount = db.Column(db.Text, nullable=False)
    grand_total_transaksi = db.Column(db.Text, nullable=False)

class TransaksiSchema(ModelSchema):
    class Meta(ModelSchema):
        sqla_session = db.session
    id_transaksi = fields.Integer(dump_only=True)
    tgl_transaksi = fields.Date(required=True)
    item_transaksi = fields.String(required=True)
    harga_transaksi = fields.String(required=True)
    qty_transaksi = fields.String(required=True)
    total_transaksi = fields.String(required=True)
    flag_transaksi = fields.String(required=True)
    discount_transaksi = fields.String(required=True)
    member_discount = fields.String(required=True)
    grand_total_transaksi = fields.String(required=True)

####################################################################
class Log(db.Model):
    __tablename__ = 'Log'
    id_log = db.Column(db.Integer, primary_key=True)
    tgl_log = db.Column(db.Date, nullable=False)
    log = db.Column(db.Text, nullable=False)
    username_in = db.Column(db.Text, nullable=False)

class LogSchema(ModelSchema):
    class Meta(ModelSchema):
        sqla_session = db.session
    id_log = fields.Integer(dump_only=True)
    tgl_log = fields.Date(required=True)
    log = fields.String(required=True)
    username_in = fields.String(required=True)
