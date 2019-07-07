import tornado.web
from pycket.session import SessionMixin

class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):
        # return self.get_secure_cookie("tudo_cookie")
        return self.session.get('tudo_cookie')

# 首页，用户上传图片的展示
class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html', img_list=[])

#单个图片详情页
class PostHandler(BaseHandler):
    def get(self,post_id):
        self.render('post.html', post_id=post_id)

class ExploreHandler(BaseHandler):
    '''最近上传的缩略图片页面'''
    def get(self):
        self.render('explore.html', img_list=[])