import pymysql as MySQLdb
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB

from . import repertory
from . import dbconfig

class DbConnection(object):
    __pool = None
    def __init__(self):
        self._conn = DbConnection.__getCoon()
        self._cursor = self._conn.cursor()

    @staticmethod
    def __getCoon():
        if DbConnection.__pool is None:
            __pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20, 
            host=dbconfig.DBHOST, port=dbconfig.DBPORT, user=dbconfig.DBUSER, passwd=dbconfig.DBPWD,
            db=dbconfig.DBNAME, use_unicode=True, charset="utf8mb4", cursorclass=DictCursor)
            return __pool.connection()
            #use_unicode=True 显示中文字符

    def getAll(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    def begin(self):
        self._conn.begin()

    def end(self, option="commit"):
        if option=="commit":
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        if isEnd==1:
            self.end("commit")
        else:
            self.end("rollback")
        self._cursor.close()
        self._conn.close()                        
                    
