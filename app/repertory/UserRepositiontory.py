from . import repertory

from ..model.User import IUserRepository
from .DbConnection import DbConnection


class  UserRepository(IUserRepository):
    def __init__(self):
        self.conn = DbConnection()

    def fetch_one_by_user_pwd(self, user, pwd):
        sql = "select * from userinfo where username='%s' and password='%s'"%(user,pwd)
        result = self.conn.getAll(sql)
        self.conn.dispose()
        return result[0]
            