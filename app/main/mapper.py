from ..infrastructure.DI import Mapper
from ..model.User import UserService
from ..repertory.UserRepositiontory import UserRepository

from ..repertory.AxfRepository import AxfRepository
from ..model.axf import AxfService
    
Mapper.register(UserService, UserRepository())
Mapper.register(AxfService, AxfRepository())

#如果把依赖注入写在这里,我没有办法调用,只能分开写在不同的地方
#注册之后是单例模式的, 在外面用吧

axf_service = AxfService()