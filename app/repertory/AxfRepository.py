from . import repertory

from ..model.axf import IAxfRepository
from .DbConnection import DbConnection

class AxfRepository(IAxfRepository):
    def __init__(self):
        self.conn = DbConnection() #创建连接

    def __del__(self):
        self.conn.dispose() #关闭连接

    def fetch_all_wheels(self):
        sql = "select * from axf_wheel"
        result = self.conn.getAll(sql)
        return result

    def fetch_all_navs(self):
        sql = "select * from axf_nav"
        result = self.conn.getAll(sql)
        return result

    def fetch_all_mustbuy(self):
        sql = "select * from axf_mustbuy"
        result = self.conn.getAll(sql)
        return result

    def fetch_all_shop(self):
        sql = "select * from axf_shop"
        result = self.conn.getAll(sql)
        return result

    def fetch_all_mainshow(self):
        sql = "select * from axf_mainshow"
        result = self.conn.getAll(sql)
        return result

        
            