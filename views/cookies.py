from flask import Flask, request, make_response, render_template, redirect, url_for, Blueprint

class Cookies():
    mod = Blueprint('cookies', __name__, url_prefix='/cookies')

    @mod.route('/')
    def index():
        return render_template("cookies/cookie.html")

    @mod.route('/getcookie/')
    def getcookie():
        username = request.cookies.get('username')
        return render_template("cookies/readcookie.html", username=username)

    @mod.route('/setcookie/', methods=['POST','GET'])
    def setcookie():
        if request.method == 'POST':
                username = request.form['username']
                response = make_response()#(render_template('readcookie.html'))
                response.set_cookie('username', username)

                return redirect(url_for('cookies.getcookie'))
