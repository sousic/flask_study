# -*- coding: UTF-8 -*-
from flask import Flask, request, session, redirect, render_template, url_for, Blueprint, escape
from flask import flash


class Session:
    mod = Blueprint('sessions', __name__, url_prefix='/sessions')

    @mod.route('/')
    def index():
        #세션 유무 확인
        if 'username' in session:
            sessionName = session['username']
        else:
            sessionName = None

        return render_template('sessions/index.html', sessionName=sessionName)

    @mod.route('/login/', methods = ['POST'])
    def login():
        if request.method == 'POST':
            #세션 저장
            session['username'] = request.form['username']

        #플래싱
        flash('로그인 성공')

        return redirect(url_for('sessions.index'))

    @mod.route('/logout/')
    def logout():
        #세션 초기화
        session.pop('username',None)
        return redirect(url_for('sessions.index'))
