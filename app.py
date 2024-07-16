import tornado.ioloop
import tornado.web
from Config.route import routes
import Config.app as App

def make_app():
    return tornado.web.Application(routes())

if __name__ == "__main__":
    app = make_app()
    app.listen(App.APP_PORT)
    tornado.ioloop.IOLoop.current().start()