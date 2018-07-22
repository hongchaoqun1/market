import json

from flask import render_template, jsonify, request  

from . import main
from .mapper import axf_service


# @main.route("/login/", methods=["POST"])
# def loginHandler():
#     data = request.get_data()
#     data_dict = json.loads(data)
#     obj = service.check_login(user=data_dict["username"], pwd=data_dict["password"], email=None)
#     print(obj.email)
#     return jsonify("ok")

# @main.route("/index/")
# def index():
#     # wheels = MainWheel.objects.all()
#     # navs = MainNav.objects.all()
#     # mustbuys = MainMustbuy.objects.all()

#     # shops = MainShop.objects.all()
#     # shops0_1 = shops[0:1]
#     # shops1_3 = shops[1:3]
#     # shops3_7 = shops[3:7]
#     # shops7_11 = shops[7:11]

#     # mainshows = MainShow.objects.all()
#     data = {
#         # "title": "首页",
#         # "wheels": wheels,
#         # "navs": navs,
#         # "mustbuys": mustbuys,
#         # "shops0_1": shops0_1,
#         # "shops1_3": shops1_3,
#         # "shops3_7": shops3_7,
#         # "shops7_11": shops7_11,
#         # "mainshows": mainshows
#     }   
#     return render_template("home/home.html", context=data)

@main.route("/wheel/")
def index():
    wheels = axf_service.get_all_wheels()
    navs = axf_service.get_all_navs()
    mustbuys = axf_service.get_all_mustbuy()
    shops = axf_service.get_all_shop()
    shops0_1 = shops[0:1]
    shops1_3 = shops[1:3]
    shops3_7 = shops[3:7]
    shops7_11 = shops[7:11]
    mainshows = axf_service.get_all_mainshow()

    data = {
        "title": "首页",
        "wheels": wheels,
        "navs": navs,
        "mustbuys": mustbuys,
        "shops0_1": shops0_1,
        "shops1_3": shops1_3,
        "shops3_7": shops3_7,
        "shops7_11": shops7_11,
        "mainshows": mainshows
    }   
    return render_template("home/home.html", mainshows = mainshows,title="首页",wheels=wheels,navs=navs,mustbuys=mustbuys,
    shops0_1=shops0_1,shops1_3=shops1_3,shops3_7=shops3_7, shops7_11= shops7_11)
    

