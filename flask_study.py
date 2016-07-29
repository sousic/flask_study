# -*- coding: UTF-8 -*-
import sys
from flask import Flask, request, make_response, render_template, redirect, url_for
from filters import flashed_helper
from views import cookies, main, fileUpload, sessions

#UTF로 인코딩 기본 인코딩 변경
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.secret_key = 'session_tester'

#필터 설정
flashed_helper.flashed_helper(app)

app.register_blueprint(cookies.Cookies.mod)
app.register_blueprint(main.Main.mod)
app.register_blueprint(fileUpload.fileUpload.mod)
app.register_blueprint(sessions.Session.mod)

fileUpload.root_path = app.root_path

if __name__ == '__main__':
    app.debug = True
    app.run()
