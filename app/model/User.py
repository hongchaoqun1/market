from ..infrastructure.DI import MyType
from . import model

#模型
class vipModel:
    VIP_TYPE = (
        {"nid":1, "caption": "金牌"},
        {"nid":2, "caption": "银牌"})

    def __init__(self, nid):
        self.nid = nid

    @property
    def caption(self):
        for item in vipModel.VIP_TYPE:
            if item["nid"] == self.nid:
                return item["caption"]    

class UserModel:
    def __init__(self,nid,username,email):
        self.nid = nid
        self.username = username
        self.email = email

#接口
class IUserRepository:
    def fetch_one_by_user_pwd(self, user, pwd):
        """
        根据用户名和密码获取对象
        :param user
        :param pwd
        :return 
        """
        pass

    def fetch_one_by_email_pwd(self, email, pwd):
        """
        根据用户名和密码获取对象
        :param email
        :param pwd
        :return
        """    
        pass

#协调
class UserService(metaclass=MyType):
    def __init__(self, user_repository):
        """
        :param user_repository:数据仓库对象
        :return:
        """
        self.userRepository = user_repository

    def check_login(self, user, email, pwd):
        if user:
            m = self.userRepository.fetch_one_by_user_pwd(user, pwd)
        else:
            m = self.userRepository.fetch_one_by_email_pwd(email, pwd)  
         
        obj = UserModel(m["id"], m["username"], m["email"])
        return obj
    
