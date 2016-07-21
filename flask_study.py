# -*- coding: UTF-8 -*-
from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)

from views import cookies
from views import main
app.register_blueprint(cookies.Cookies.mod)
app.register_blueprint(main.Main.mod)

if __name__ == '__main__':
    app.debug = True
    app.run()