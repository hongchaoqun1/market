from ..infrastructure.DI import MyType
from . import model

#模型类
class AxfModels:
    def __init__(self,nid,img, name, trackid):
        self.id = nid
        self.img = img
        self.name = name
        self.trackid = trackid

class WheelsModel(AxfModels):
    pass

class NavsModel(AxfModels):
    pass

class MustBuyModel(AxfModels):
    pass      

class ShopModel(AxfModels):
    pass

class MainShowShowmodel:
    def __init__(self, nid,img, name, trackid,categoryid,brandname,img1,childcid1,productid1,
                longname1,price1,marketprice1,img2,childcid2,
                productid2,longname2,price2,marketprice2,img3,
                childcid3,productid3,longname3,price3,marketprice3):
        self.id = nid
        self.img = img
        self.name = name
        self.trackid = trackid
        self.categoryid = categoryid
        self.brandname = brandname
        self.img1 = img1
        self.childcid1 = childcid1
        self.productid1 = productid1
        self.longname1 = longname1
        self.price1 = price1
        self.marketprice1 = marketprice1
        self.img2 = img2
        self.childcid2 = childcid2
        self.productid2 = productid2
        self.longname2 = longname2
        self.price2price2 = price2
        self.marketprice2 = marketprice2
        self.img3 = img3
        self.childcid3 = childcid3
        self.productid3 = productid3
        self.longname3 = longname3
        self.price3 = price3
        self.marketprice3 = marketprice3

#接口类   
class IAxfRepository:
    def fetch_all_wheels(self):
        """
        获取所有wheels的接口
        """
        pass

    def fetch_all_navs(self):
        pass

    def fetch_all_mustbuy(self):
        pass

    def fetch_all_shop(self):
        pass

    def fetch_all_mainshow(self):
        pass

#服务类
class AxfService(metaclass=MyType):
    def __init__(self, axf_repository):
        self.axfRepository = axf_repository

    def get_result(self, reList, reModel):
        obj = []
        for i in reList:
            line = reModel(i["id"], i["img"], i["name"], i["trackid"])
            obj.append(line)
        return obj
            
    def get_all_wheels(self):
        m = self.axfRepository.fetch_all_wheels() #fetchall 返回的是一个列表,里面是字典
        obj = self.get_result(m, WheelsModel)
        # for i in m:
        #     w = WheelsModel(i["id"], i["img"], i["name"], i["trackid"])
        #     obj.append(w)
        return obj

    def get_all_navs(self):
        result = self.axfRepository.fetch_all_navs()
        obj = self.get_result(result, WheelsModel)
        return obj

    def get_all_mustbuy(self):
        result = self.axfRepository.fetch_all_mustbuy()
        obj = self.get_result(result, MustBuyModel)
        return obj

    def get_all_shop(self):
        result = self.axfRepository.fetch_all_shop()
        obj = self.get_result(result, ShopModel)
        return obj

    def get_all_mainshow(self):
        result = self.axfRepository.fetch_all_mainshow()
        obj = []
        for kwargs in result:
            line = MainShowShowmodel(kwargs["id"], kwargs["img"], kwargs["name"], kwargs["trackid"],
            kwargs["categoryid"],kwargs["brandname"],kwargs["img1"],kwargs["childcid1"],kwargs["productid1"],
            kwargs["longname1"],kwargs["price1"],kwargs["marketprice1"],kwargs["img2"],kwargs["childcid2"],
            kwargs["productid2"],kwargs["longname2"],kwargs["price2"],kwargs["marketprice2"],kwargs["img3"],
            kwargs["childcid3"],kwargs["productid3"],kwargs["longname3"],kwargs["price3"],kwargs["marketprice3"])
            obj.append(line)
        return obj
    
