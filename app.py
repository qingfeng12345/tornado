import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options
from handlers import main

# 定义端口信息
define('port', default='8000', help='Listening port', type=int)


class application(tornado.web.Application):
    def __init__(self):
        # handlers 定义路由
        handlers = [(r"/", main.IndexHandler),
                    (r"/explore", main.ExploreHandler),
                    (r"/post/(?P<post_id>[0-9]+)", main.PostHandler),
                    ]
        settings = dict(debug = True,
                        template_path = 'templates',
                        static_path = 'picture',
                        # autoescape = None,
                        cookie_secret='qwdegijklssasxvlmn',  #需要使用get_secure_cookie函数
                        login_url='/submit',
                        pycket={
                             'engine': 'redis',
                            'storage': {
                                'host': 'localhost',
                                'port': 6379,
                                # 'password': '',
                                'db_sessions': 5,  #redis db index
                                'db_notifications': 11,
                                'max_connections': 2 ** 30,
                            },
                        'cookies': {
                            'expires_days': 30,
                            },
                        }
                        )
        super().__init__(handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = application()
    app.listen(options.port)
    print("Server start on port {}" .format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()