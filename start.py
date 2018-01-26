# ！/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import datetime


class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('index.html', t1=datetime.datetime.now())

    def post(self, *args, **kwargs):
        user = self.get_argument('username')
        pwd = self.get_argument('password')
        if user == "alex" and pwd == "123":
            self.redirect("http://www.baidu.com")  # 跳转百度的url

        else:
            self.write('登录失败，请重新输入')  # 返回字符串

class LoginHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('login.html', state="")

    def post(self, *args, **kwargs):
        user = self.get_argument('username')
        pwd = self.get_argument('password')
        if user == "alex" and pwd == "123":
            self.redirect("http://www.baidu.com")  # 跳转百度的url

        else:
            self.write('登录失败，请重新输入')  # 返回字符串


settings = {
    'template_path': 'views',
}

application = tornado.web.Application([
    (r"/login", LoginHandler),
    (r"/index", IndexHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

