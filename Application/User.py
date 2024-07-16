from typing import Any
import tornado
from tornado.httputil import HTTPServerRequest
from tornado.web import Application
from Services.UserAggregationService import UserAggregationService
from Common.Function import ReturnDict
from Common.Share.BaseController import Handler

from datetime import datetime
class UserHandler(Handler):
    def __init__(self, application: Application, request: HTTPServerRequest, **kwargs: Any) -> None:
        self.rootAggService = UserAggregationService()
        super().__init__(application, request, **kwargs)

    async def get(self):
        now = datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S.%f"))
        data = self.rootAggService.getUserInfo()
        _return = await ReturnDict(self.redis,self.request_context)
        self.write(_return)
        _end = datetime.now()
        print(_end.strftime("%Y-%m-%d %H:%M:%S.%f"))

    async def post(self):
        self.write({'code':0,'msg':'ok'})

class UserAvatorHandler(Handler):
    async def get(self):
        print(self.get_query_arguments('param_name'))
        self.write({'code':0,'msg':'ok'})        