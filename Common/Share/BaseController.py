from typing import Any
import tornado
from tornado.httputil import HTTPServerRequest
from tornado.web import Application
from Common.Function import RequestContext
from Common.Redis import init_redis, heartbeat
import tornado.ioloop
import asyncio

class Handler(tornado.web.RequestHandler):
    def __init__(self, application: Application, request: HTTPServerRequest, **kwargs: Any) -> None:
        _request_context = RequestContext(request.uri)
        _request_context['protocol'] = request.protocol
        _request_context['host'] = request.host
        _request_context['method'] = request.method
        _request_context['uri'] = request.uri
        _request_context['version'] = request.version
        _request_context['remote_ip'] = request.remote_ip
        self.request_context = _request_context
        self.redis = init_redis()
        # 启动心跳检测任务（每隔一段时间执行一次心跳检测）
        tornado.ioloop.PeriodicCallback(lambda: asyncio.create_task(heartbeat(self.redis)), 5000).start()
        super().__init__(application, request, **kwargs)

    def initialize(self, session):
        self.session = session