from datetime import datetime

from sqlalchemy.ext.declarative import AbstractConcreteBase, declared_attr
from app import db

class UserInfo(db.Model):
    """
    用户信息
    """
    __tablename__ = "userinfo"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(64))
    email = db.Column(db.String(64))
    user_type = db.Column(db.Integer)
    vip_type = db.Column(db.Integer)
    merchant = db.relationship('Merchant', backref="userinfo", lazy="dynamic")
    
    member_since = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    

class Merchant(db.Model):
    """
    商户
    """
    __tablename__ = "merchant"
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(8), index=True)
    business_modile = db.Column(db.String(16))
    qq = db.Column(db.String(16))
    backend_modile = db.Column(db.String(16))
    user_id = db.Column(db.Integer, db.ForeignKey("userinfo.id"))

    name = db.Column(db.String(64), index=True)
    business_phone = db.Column(db.String(16))
    backend_phone = db.Column(db.String(16))
    address = db.Column(db.String(128))


# class Main(AbstractConcreteBase, db.Model):
#     img = db.Column(db.String(200))
#     name = db.Column(db.String(64))
#     trackid = db.Column(db.Integer,default=0)

#     __mapper_args__ = {
#        'polymorphic_identity':'main',
#         'polymorphic_on':type
#     }

class MainWheel(db.Model):
    __tablename__ = "axf_wheel"
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(64))
    trackid = db.Column(db.Integer,default=0)
    
class MainNav(db.Model):
    __tablename__ = "axf_nav"
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(64))
    trackid = db.Column(db.Integer,default=0)

class MainMustbuy(db.Model):
    __tablename__ = "axf_mustbuy"
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(64))
    trackid = db.Column(db.Integer,default=0)

class MainShop(db.Model):
    __tablename__ = "axf_shop"
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(64))
    trackid = db.Column(db.Integer,default=0)

class MainShow(db.Model):
    __tablename__ = "axf_mainshow"
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(64))
    trackid = db.Column(db.Integer,default=0)
    categoryid = db.Column(db.Integer,default=0)
    brandname = db.Column(db.String(32))
    img1 = db.Column(db.String(200))
    childcid1 = db.Column(db.Integer,default=0)
    productid1 = db.Column(db.Integer,default=0)
    longname1 = db.Column(db.String(100))
    price1 = db.Column(db.Integer,default=0)
    marketprice1 = db.Column(db.Integer,default=0)
    img2 = db.Column(db.String(200))
    childcid2 = db.Column(db.Integer,default=0)
    productid2 = db.Column(db.Integer,default=0)
    longname2 = db.Column(db.String(100))
    price2 = db.Column(db.Integer,default=0)
    marketprice2 = db.Column(db.Integer,default=0)
    img3 = db.Column(db.String(200))
    childcid3 = db.Column(db.Integer,default=0)
    productid3 = db.Column(db.Integer,default=0)
    longname3 = db.Column(db.String(100))
    price3 = db.Column(db.Integer,default=0)
    marketprice3 = db.Column(db.Integer,default=0)

class FoodType(db.Model):
    __tablename__ = "axf_foodtypes"
    id = db.Column(db.Integer, primary_key=True)
    typeid = db.Column(db.Integer,default=0)
    typename = db.Column(db.String(32))
    childtypenames = db.Column(db.String(200))
    typesort = db.Column(db.Integer,default=0)


class Goods(db.Model):
    __tablename__ = "axf_goods"
    id = db.Column(db.Integer, primary_key=True)
    productid = db.Column(db.Integer,default=0)
    productimg = db.Column(db.String(200))
    productname = db.Column(db.String(100))
    productlongname = db.Column(db.String(200))
    isxf = db.Column(db.Boolean,default=False)
    pmdesc = db.Column(db.Integer,default=0)
    specifics = db.Column(db.String(100))
    price = db.Column(db.Float,default=0)
    marketprice = db.Column(db.Float,default=0)
    categoryid = db.Column(db.Integer,default=0)
    childcid = db.Column(db.Integer,default=0)
    childcidname = db.Column(db.String(32))
    dealerid = db.Column(db.Integer,default=0)
    storenums = db.Column(db.Integer,default=0)
    productnum = db.Column(db.Integer,default=0)

class User(db.Model):
    __tablename__ = 'axf_user'
    id = db.Column(db.Integer, primary_key=True)
    u_name =db.Column(db.String(16), unique=True)
    u_password =db.Column(db.String(128))
    u_email =db.Column(db.String(64), unique=True)
    is_active =db.Column(db.Boolean,default=False)
    is_delete =db.Column(db.Boolean,default=False)
    u_icon =db.Column(db.String(128))

