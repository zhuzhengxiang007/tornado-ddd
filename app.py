import tornado.ioloop
import tornado.web
from Config.route import routes
import Config.app as App
import asyncio
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Config.mysql as Mysql

# 创建异步引擎
DATABASE_URL = f"mysql+aiomysql://{Mysql.MYSQL_USERNAME}:{Mysql.MYSQL_PASSWORD}@{Mysql.MYSQL_HOST}/{Mysql.MYSQL_DATABASE}?charset=utf8"
engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_recycle=3600)

# 创建会话
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

def make_app():
    return tornado.web.Application(routes(async_session))

if __name__ == "__main__":
    app = make_app()
    app.listen(App.APP_PORT)
    tornado.ioloop.IOLoop.current().start()